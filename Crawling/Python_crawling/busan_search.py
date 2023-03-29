import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate
import seaborn as sns
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import json


client_id = "6edzCNnNWRuAcEfH4xKc"
client_secret = "T6ZF8xVRNj"
keywordGroups = []
url = "https://openapi.naver.com/v1/datalab/search"



def korean_font():
    plt.rc('font',family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


def busan():
    tabulate.WIDE_CHARS_MODE = False
    df = replace()
    # df = pd.read_csv('C:\부산맛집.csv',encoding='cp949')
    df = df[['영업신고증업태명','식당명','지번주소','식당대표전화번호']]
    # df.to_excel('부산맛집.xlsx') # 부산 맛집 엑셀 저장
    df = df.dropna(axis=0)
    df.columns = ['분류','식당','주소','전화번호']

    while True:
        try:
            me = main_menu()
            if me == '1':
                enter = input('원하는 음식종류를 입력하세요.\n(예:한식,중식,일식,분식,치킨,횟집,고깃집,카페등)\n')
                search = df.query(f'분류 == "{enter}"')
                search = search.sample(100,replace=True)
                print(tabulate(search, headers='keys',tablefmt='fancy_grid',showindex=False,stralign='center'))
                korean_font()
                plot()
            elif me == '2':
                tour()
                rdf = tour()
                plot1(rdf)
            elif me == '3':
                dic_data = get_url2()
                parsed_data = data_parse(dic_data)
                json_write(parsed_data)
                data_visualization(parsed_data)
            elif me == '4':
                print(f"데이터를 다운 받는 중 입니다.{len(keywordGroups) / 5 * 100}%")
                print(df2)
                plot_monthly_trend_line()

            elif me == '5':
                print('종료')
                exit()

        except ValueError:
            print('없는 음식입니다 다시 실행해주세요.(예:한식,중식,일식,분식,치킨,횟집,고깃집,카페등)')
            return df
def plot():
    df = replace()
    print(df['영업신고증업태명'].value_counts())
    plt.figure(figsize=(10, 8))
    sns.countplot(data=df, x="영업신고증업태명",
                  order=df["영업신고증업태명"].value_counts().index)
    plt.title('부산광역시 음식점 분류 그래프')
    plt.xlabel('')
    plt.ylabel('음식점의 개수')

    plt.show()



def replace():
    df = pd.read_csv('C:\부산맛집.csv', encoding='cp949')
    df = df.replace('호프/통닭', '치킨')
    df = df.replace('회집', '횟집')
    df = df.replace('식육(숯불구이)', '고깃집')
    df = df.replace('중국식', '중식')
    df = df.replace('커피숍', '카페')
    df = df.replace('유원지', '기타')
    df = df.replace('공항', '기타')
    df = df.replace('극장', '기타')
    df = df.replace('관광호텔', '기타')
    df = df.replace('감성주점', '기타')
    df = df.replace('고속도로', '기타')
    df = df.replace('철도역구내', '기타')
    df = df.replace('푸드트럭', '기타')
    df = df.replace('백화점', '기타')
    df = df.replace('냉면집', '기타')
    df = df.replace('외국음식전문점(인도,태국등)', '기타')
    df = df.replace('뷔페식', '기타')
    df = df.replace('라이브카페', '카페')
    df = df.replace('떡카페', '카페')
    df = df.replace('전통찻집', '카페')
    df = df.replace('김밥(도시락)', '한식')
    df = df.replace('탕류(보신용)', '기타')
    df = df.replace('아이스크림', '카페')
    df = df.replace('복어취급', '기타')
    df = df.replace('일반조리판매', '기타')
    df = df.replace('기타 휴게음식점', '기타')
    df = df.replace('제과점영업', '기타')
    df = df.replace('정종/대포집/소주방', '기타')
    df = df.replace('기타(편의점)', '기타')
    df = df.replace('패밀리레스토랑', '기타')
    df = df.replace('다방', '카페')
    df = df.replace('패스트푸드', '기타')
    return df

def tour():
    baseurl = 'http://apis.data.go.kr/6260000/AttractionService/getAttractionKr'
    param = '?serviceKey=Wa7m7zwPssEEuvCmyllNkb2oMvlUjXw8fAgXRGDhOGrQ3bIP64oBnXXkVpRrd5XU%2FK6AO0OSL5gAfBpH%2FJ4PYg%3D%3D&pageNo=1&numOfRows=100'
    url = baseurl + param
    print(url)
    resxml = urlopen(url)
    res_data = resxml.read()
    soup = BeautifulSoup(res_data, 'lxml-xml')
    items = soup.findAll('item')
    #print(soup)
    total_list = []
    count = 0
    for te in items:
        MAIN_TITLE = te.find('MAIN_TITLE').text
        GUGUN_NM = te.find('GUGUN_NM').text
        MIDDLE_SIZE_RM1 =te.find('MIDDLE_SIZE_RM1').text
        TRFC_INFO = te.find('TRFC_INFO').text
        HOMEPAGE_URL = te.find('HOMEPAGE_URL').text
        ITEMCNTNTS = te.find('ITEMCNTNTS').text
        count += 1
        print('번호',count)
        print('관광지:', MAIN_TITLE)
        print('구군:', GUGUN_NM)
        print('편의시설:', MIDDLE_SIZE_RM1)
        print('교통정보:', TRFC_INFO)
        print('홈페이지:', HOMEPAGE_URL)
        print('상세내용:', ITEMCNTNTS)
        print('==================================================================')
        dic = {'관광지':MAIN_TITLE, '구군':GUGUN_NM, '편의시설': MIDDLE_SIZE_RM1,
               '교통정보': TRFC_INFO, '홈페이지': HOMEPAGE_URL }
        total_list.append(dic)

    df1 = pd.DataFrame.from_dict(total_list)
    #print(df)
    writer = pd.ExcelWriter('부산관광지2.xlsx',
                               engine='xlsxwriter') # 부산 관광지 엑셀 저장
    df1.to_excel(writer, sheet_name='Sheet1')
    writer.close()
    return df1

def plot1(df1):
    x = np.arange(15)
    youngdogu = df1[df1['구군'] == '영도구']['구군'].value_counts()
    giznag = df1[df1['구군'] == '기장군']['구군'].value_counts()
    donggu = df1[df1['구군'] == '동구']['구군'].value_counts()
    dongregu = df1[df1['구군'] == '동래구']['구군'].value_counts()
    junggu = df1[df1['구군'] == '중구']['구군'].value_counts()
    seogu = df1[df1['구군'] == '서구']['구군'].value_counts()
    namgu = df1[df1['구군'] == '남구']['구군'].value_counts()
    haeun = df1[df1['구군'] == '해운대구']['구군'].value_counts()
    suyeong = df1[df1['구군'] == '수영구']['구군'].value_counts()
    saha = df1[df1['구군'] == '사하구']['구군'].value_counts()
    buk = df1[df1['구군'] == '북구']['구군'].value_counts()
    sasang = df1[df1['구군'] == '사상구']['구군'].value_counts()
    gang = df1[df1['구군'] == '강서구']['구군'].value_counts()
    jingu = df1[df1['구군'] == '부산진구']['구군'].value_counts()
    geum = df1[df1['구군'] == '금정구']['구군'].value_counts()

   #print('개수:', type(youngdogu.loc['영도구']))
    gugun = ['영도구', '기장군', '동구','동래구','중구','서구','남구','해운대구','수영구','사하구','북구','사상구','강서구','부산진구','금정구']
    values = [youngdogu.loc['영도구'], giznag.loc['기장군'],  donggu.loc['동구'],
              dongregu.loc['동래구'], junggu.loc['중구'], seogu.loc['서구'],
              namgu.loc['남구'], haeun.loc['해운대구'], suyeong.loc['수영구'],saha.loc['사하구'],
              buk.loc['북구'], sasang.loc['사상구'],  gang.loc['강서구'],
              jingu.loc['부산진구'],geum.loc['금정구']]
    colors = ['dodgerblue', 'dodgerblue', 'dodgerblue','dodgerblue','dodgerblue','dodgerblue','dodgerblue',
              'dodgerblue','dodgerblue','dodgerblue','dodgerblue','dodgerblue','dodgerblue','dodgerblue','dodgerblue']

    plt.rcParams["figure.figsize"] = (10, 8)
    plt.bar(x, values, color=colors)

    plt.xticks(x, gugun)
    plt.title('구군별 관광지 수', pad=40, size=30)
    plt.ylabel('관광지 수')

    print('구군별 관광지 수')
    gun = df1['구군'].value_counts()
    print(gun)
    plt.show()

def main_menu():
    print('==================================')
    print(' 부산광역시에 오신것을 환영합니다.')
    print('==================================')
    print(' 1. 부산광역시 음식점 소개\n')
    print(' 2. 부산광역시 인기 관광지\n')
    print(' 3. 부산광역시 축제 일정\n')
    print(' 4. 부산광역시 월별 검색어 트렌드\n')
    print(' 5. 종료')
    print('=================================')
    menu = input('메뉴 입력:')
    return menu

def get_data(url, startDate, endDate, timeUnit, keywordGroups, device, ages, gender):
    # 데이터 요청 사항 입력
    global client_id, client_secret
    body = json.dumps({
        "startDate": startDate,
        "endDate": endDate,
        "timeUnit": timeUnit,
        "keywordGroups": keywordGroups,
        "device": device,
        "ages": ages,
        "gender": gender
    }, ensure_ascii=False)

    # 불러오기
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        # Json Result
        result = json.loads(response.read())
        df2 = pd.DataFrame(result['results'][0]['data'])[['period']]
        for i in range(len(keywordGroups)):
            tmp = pd.DataFrame(result['results'][i]['data'])
            tmp = tmp.rename(columns={'ratio': result['results'][i]['title']})
            df2 = pd.merge(df2, tmp, how='left', on=['period'])
        df2 = df2.rename(columns={'period': '날짜'})
        df2['날짜'] = pd.to_datetime(df2['날짜'])
        # df2.to_excel('부산.xlsx') # 부산 검색어 트렌드 엑셀 저장

    else:
        print("Error Code:" + rescode)

    return df2


def add_keyword_groups(group_dict):
    global keywordGroups
    keyword_gorup = {
        'groupName': group_dict['groupName'],
        'keywords': group_dict['keywords']
    }
    keywordGroups.append(keyword_gorup)
    # print(f"데이터를 다운 받는 중 입니다.{len(keywordGroups) / 5 * 100}%")


def plot_monthly_trend_line():
    year = df2['날짜'][0].year
    fig = plt.figure(figsize=(12, 6))
    plt.title(f'{year}년 - 월 별 검색어 트렌드', size=20, loc='center')

    sns.lineplot(x='월', y=df2.columns[1], label=df2.columns[1], data=df2, err_style="bars")
    sns.lineplot(x='월', y=df2.columns[2], label=df2.columns[2], data=df2, err_style="bars")
    sns.lineplot(x='월', y=df2.columns[3], label=df2.columns[3], data=df2, err_style="bars")
    sns.lineplot(x='월', y=df2.columns[4], label=df2.columns[4], data=df2, err_style="bars")

    plt.legend(loc='upper right')
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.show()


keyword_group_set = {
    'keyword_group_1': {'groupName': "관광", 'keywords': ["관광", "명소", "부산"]},
    'keyword_group_2': {'groupName': "레저", 'keywords': ["레저", "부산"]},
    'keyword_group_3': {'groupName': "숙소", 'keywords': ["숙소", "분위기", "부산"]},
    'keyword_group_4': {'groupName': "음식점", 'keywords': ["음식점", "부산"]},
    'keyword_group_5': {'groupName': "시장", 'keywords': ["시장", "부산"]}
}

# 요청 파라미터 설정
startDate = "2022-01-01"
endDate = "2022-12-31"
timeUnit = 'date'
device = ''
ages = []
gender = ''

# 데이터 프레임 정의
add_keyword_groups(keyword_group_set['keyword_group_1'])
add_keyword_groups(keyword_group_set['keyword_group_2'])
add_keyword_groups(keyword_group_set['keyword_group_3'])
add_keyword_groups(keyword_group_set['keyword_group_4'])
add_keyword_groups(keyword_group_set['keyword_group_5'])

df2 = get_data(url, startDate, endDate, timeUnit, keywordGroups, device, ages, gender)
df2['월'] = df2['날짜'].apply(lambda x: x.month)
# print(df2)

def add_value_label(x_list, y_list):
    for i in range(0, len(x_list)):
        plt.text(i, y_list[i], y_list[i], horizontalalignment="center", verticalalignment='bottom')


def get_url2():
    numofRows = 50
    pageNo = 1
    serviceKey = 'VNFJwJEGxN%2F8HoNCl3v3Sd3u1EtmWsKspt4FblKzZ4J9UZv3YK40Q0hQkZxWZc%2BI5Z5YMMgb89xtV2Nbhn3iow%3D%3D'
    baseURL = 'http://apis.data.go.kr/6260000/FestivalService/getFestivalKr'
    param = f'?serviceKey={serviceKey}'
    param += f'&numOfRows={numofRows}'
    param += f'&pageNo={pageNo}'
    param += f'&resultType=json'
    URL = baseURL + param
    # print(URL)

    try:
        request = urllib.request.Request(URL)
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            ret_data = response.read().decode('utf-8')
            # print(ret_data)
            # print(type(ret_data))
            dic_data = json.loads(ret_data)
            # print(dic_data)
            # print(type(dic_data))
            #
            # print(dic_data['getFestivalKr'])
            # print(type(dic_data['getFestivalKr']))
            #
            # print(dic_data['getFestivalKr']['header'])
            # print(type(dic_data['getFestivalKr']['header']))
            #
            # print(dic_data['getFestivalKr']['item'])
            # print(type(dic_data['getFestivalKr']['item']))
            #
            # print(dic_data['getFestivalKr']['item'][0])
            # print(type(dic_data['getFestivalKr']['item'][0]))
            #
            # print(dic_data['getFestivalKr']['item'][0]['MAIN_TITLE'])
            # print(type(dic_data['getFestivalKr']['item'][0]['MAIN_TITLE']))

            return dic_data

    except Exception as ex:
        print('HTTP 에러:', ex)
        
def data_parse(dic_data):
    if dic_data['getFestivalKr']['header']['message'] == 'NORMAL_CODE':
        # print(dic_data['getFestivalKr']['item'])
        # print(dic_data['getFestivalKr']['item'][0])
        # print(dic_data['getFestivalKr']['item'][1])
        # print(dic_data['getFestivalKr']['item'][1]['UC_SEQ'])
        i = 0
        dic_parse_data = {}
        for n in dic_data['getFestivalKr']['item']:
            title = dic_data['getFestivalKr']['item'][i]['MAIN_TITLE']
            title = title.replace('(한,영, 중간,중번,일)','').replace('(한, 영)','')\
                .replace('(한,영,중간,중번,일)','').replace('(한, 영, 중간, 중번, 일)','').replace('(한, 영, 중간,중번,일)','')

            place = dic_data['getFestivalKr']['item'][i]['GUGUN_NM']

            if dic_data['getFestivalKr']['item'][i]['USAGE_DAY'] != '':
                date = dic_data['getFestivalKr']['item'][i]['USAGE_DAY']
            else:
                date = dic_data['getFestivalKr']['item'][i]['USAGE_DAY_WEEK_AND_TIME']

            date = date.replace('프로그램별 상이(홈페이지 참조)', '').replace('프로그램 별 상이(홈페이지 참조)', '')\
                .replace('프로그램별 상이','').replace('부처님 오신 날','5월').replace('정월대보름','2월').replace('축제 ','')\
                .replace('매년','2022년').replace('2022.','2022년').replace('2022년 ','').replace('2022년','')\
                .replace('월','.').replace('\n','').split('.')
            date = date[0]

            # print(title)
            # print(place)
            # print(date)

            dic_parse_data[i+1] ={'축제이름' : title, '축제장소' : place, '축제당월' : date}
            # print(dic_parse_data[i+1])
            print('축제:',dic_parse_data[i+1]['축제이름'])
            print('장소:','부산광역시',dic_parse_data[i + 1]['축제장소'])
            print('축제가 열리는 월:', dic_parse_data[i + 1]['축제당월']+'월')
            print('==============================')

            i+=1
    df_parse_data = pd.DataFrame(dic_parse_data)
    df_parse_data_change = df_parse_data.T
    # df_parse_data.plot.bar()
    # plt.show()
    # print(df_parse_data_change)

    return df_parse_data_change

def json_write(df_parse_data_change):
    writer = pd.ExcelWriter('부산 축제.xlsx', engine='xlsxwriter') # 부산축제 엑셀 저장
    df_parse_data_change.to_excel(writer, sheet_name='Sheet1')
    writer.close()
    # print('json_write 성공')

def data_visualization(df_parse_data_change):
    korean_font()
    x = np.arange(12)
    # print(df_parse_data_change['축제당월'] == '1')
    # print(len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '5']))

    january = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '1'])
    february = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '2'])
    march = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '3'])
    april = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '4'])
    may = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '5'])
    june = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '6'])
    july = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '7'])
    august = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '8'])
    september = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '9'])
    october = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '10'])
    november = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '11'])
    december = len(df_parse_data_change.loc[df_parse_data_change['축제당월'] == '12'])

    # print(may)
    # print(type(may))

    month = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
    values = [january, february, march, april, may, june, july, august, september, october, november, december]
    # print(values[january])
    colors = ['dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue',
              'dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue', 'dodgerblue']

    plt.figure(figsize=(10, 8))
    plt.bar(x, values, color=colors)
    plt.xticks(x, month)
    add_value_label(month, values)
    plt.title('월별 축제 수', pad=40, size=30)
    plt.ylabel('축제 수')
    plt.show()


if __name__=='__main__':
    korean_font()
    busan()
    
    # plot()



