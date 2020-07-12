import requests

API_URL_ALL_DATA = 'https://api.covid19india.org/data.json'
API_URL_DISTRICT_WISE = 'https://api.covid19india.org/state_district_wise.json'

response = requests.get(API_URL_ALL_DATA)


def get_daily_stats(response):
    try:
        all_cases_data_list = response.json()['cases_time_series']
        latest_cases_data = all_cases_data_list[len(all_cases_data_list) - 1]
        formatted_data = f'''
            COVID INDIA DAILY STATS:
            AS of {latest_cases_data['date']}
            ******************************
            Total Confirmeed Cases : {latest_cases_data['totalconfirmed']}
            Total Recovered Cases : {latest_cases_data['totalrecovered']}
            Total Deaths Reported: {latest_cases_data['totaldeceased']}
            Confirmed Cases Yesterday: {latest_cases_data['dailyconfirmed']}
            Confirmed Recovered Cases Yesterday: {latest_cases_data['dailyrecovered']}
            Deaths Reported Yesterday: {latest_cases_data['dailydeceased']}
            ******************************
        '''
        print(formatted_data)
    except:
        print('An error occurred while processing data')


def get_top5_states_with_active_cases(response):
    try:
        all_states_data_list = response.json()['statewise']
        all_states_data_list.sort(
            key=lambda x: int(x['active']), reverse=True)
        top5_active_states = all_states_data_list[1:6]
        print('Top 5 states with most active cases in India:')
        for index, state in enumerate(top5_active_states):
            formatted_data = f'''
            ********{index + 1}*************
            State: {state['state']}
            Active: {state['active']}
            Total Confirmed : {state['confirmed']} 
            ***************************
        
            '''
            print(formatted_data)
    except Exception as error:
        print(f'An error occured while processing data, {error}')


if __name__ == '__main__':
    get_daily_stats(response)
    get_top5_states_with_active_cases(response)
