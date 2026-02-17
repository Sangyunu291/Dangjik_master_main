from event_managers import *

def load_data(worker_file, exception_file):
    worker_data = []
    
    # 1. 인명부 로드
    with open(worker_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            worker_data.append(row)
            
    # 2. 열외 명단 로드 (데이터 로직 내에서 활용하기 위해 리스트화)
    exceptions = []
    with open(exception_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            exceptions.append(row)
            
    return worker_data, exceptions


def main():
    try:
        worker_data, exceptions = load_data('./data/worker_list.csv', './data/exception_list.csv')
    except FileNotFoundError as e:
        return f"CRITICAL_ERROR: CSV 파일을 찾을 수 없습니다. ({e})"

    all_event_list =  list(input().split())

    date_range = ('2026-01-05', '2026-02-06')
    
    
    engine = MainEngine(date_range, worker_data, exceptions)
    engine.exp_manager.runManage()
    
    for event in all_event_list:
        file_name = f"add_{event}.csv"
        if event == '위병부조장': engine.sg_manager.runManage('25-760034')
        elif event == '식기': engine.dish_manager.runManage('25-760013', '2026-02-06')
        elif event == '불침번': engine.night_manager.runManage('25-760033')
        elif event == '초병': engine.st_manager.runManage('25-760002', '25-760040')
        elif event == 'CCTV': engine.cctv_manager.runManage('25-760008')
        engine.export_result_as_file(file_name)
        
    
    all_event_list.reverse()

    for event in all_event_list:
        file_name = f"delete_{event}.csv"
        if event == '위병부조장': engine.sg_manager.delManage()
        elif event == '식기': engine.dish_manager.delManage()
        elif event == '불침번': engine.night_manager.delManage()
        elif event == '초병': engine.st_manager.delManage()
        elif event == 'CCTV': engine.cctv_manager.delManage()
        engine.export_result_as_file(file_name)
        

if __name__ == "__main__":
    main()