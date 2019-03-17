import random
import copy

PAGE_MEMORY = 4
INTERVAL = 1


def time_up(page_list):
    for p in page_list:
        p['time'] += INTERVAL


def print_list(page_list):
    page_num = []
    for p in page_list:
        page_num.append(int(p['No']))
    print('序列为：', end=' ')
    print(page_num)




####################改进型Clock置换算法#############################

def obsolete_page(page_list):
    while True:
        for page in page_list:
            if page['visited'] == False and page['modified'] == False:
                return page
        for page_ in page_list:
            if page_['visited'] == False and page_['modified'] == True:
                return page_
        for _page in page_list:
            _page['visited'] = False


def getIndex(p, page_list):
    i = 0
    for pages_ in page_list:
        if p['No'] == pages_['No']:
            return i
        i += 1
    return 0


def Improved_Clock(pages_):
    pages = copy.deepcopy(pages_)
    print('')
    print('页面请求序列为 8 9 10 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1')
    print('############ Improved_Clock ################')
    page_list = []
    for p in pages:
        page_list_data = []
        if len(page_list) < PAGE_MEMORY:
            page_list.append(p)
        else:
            for page_ in page_list:
                page_list_data.append(page_['No'])
            if p['No'] not in page_list_data:
                _page = obsolete_page(page_list)
                print('----Remind-----: 新页表%d将会替换页表%d' % (_page['No'], p['No']))
                page_list.remove(_page)
                page_list.append(p)
            else:
                print('----Remind-----: 页表%d已存在，绝对地址为%d' % (
                page_list[getIndex(p, page_list)]['No'], 1024 * getIndex(p, page_list)))
                page_list[getIndex(p, page_list)]['visited'] = True
        print_list(page_list)


def init(pages):
    for p in pages:
        p['time'] = 0
        p['visited'] = False
        a = random.random()
        if a < 0.5:
            p['modified'] = False
        else:
            p['modified'] = True  # 被访问过


if __name__ == '__main__':
    pages = [
        {'No': 8}, {'No': 9}, {'No': 10}, {'No': 7}, {'No': 0}, {'No': 1}, {'No': 2},
        {'No': 0}, {'No': 3}, {'No': 0}, {'No': 4}, {'No': 2}, {'No': 3}, {'No': 0},
        {'No': 3}, {'No': 2}, {'No': 1}, {'No': 2}, {'No': 0}, {'No': 1}, {'No': 7},
        {'No': 0}, {'No': 1}
    ]

    init(pages)

    FIFO(pages)

    LRU(pages)

    Improved_Clock(pages)
