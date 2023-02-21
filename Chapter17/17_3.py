from concurrent import futures

from flags import *

MAX_WORKERS = 20

def down_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    wokers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(wokers) as executor:
        res = executor.map(down_one, sorted(cc_list))

if __name__ == "__main__":
    main(download_many)