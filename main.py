import redis
import streamlit as st
import os

NO_DESTINATION_MSG = '**行先は未定です**'
HOST_NAME = os.environ['HOST_NAME']
ACCESS_KEY = os.environ['PASSWORD']

# DB接続
redis_conn = redis.StrictRedis(
        host=HOST_NAME,
        port=6380,
        db=0,
        password=ACCESS_KEY,
        ssl=True
    )


# 表示処理
def main():
    st.title('[東京版] 指令さんぽゲーム～次の行先はどこ？～')

    st.markdown('現在のデータソース')

    '''
    下記の条件を満たした駅のみが登録されています。
    - 東京都内の駅
    - 駅名に「橋」が入ってる
    '''

    # 現在の行先を表示
    destination = redis_conn.get('destination')
    st.markdown('### 現在の行先')

    # 行先表示。行先が未定の場合は未設定メッセージを表示
    next_station = st.empty()

    if destination is None or destination == b'':
        next_station.markdown(NO_DESTINATION_MSG)
    else:
        destination = destination.decode('utf-8')
        next_station.write(destination)

    # このボタンを押すと行先がゴールとして達成済みセットに登録される
    goal = st.empty()
    if goal.button('ゴール!'):
        if destination:
            redis_conn.sadd('achieved', destination)
            redis_conn.delete('destination')
            next_station.markdown(NO_DESTINATION_MSG)
        else:
            st.warning(NO_DESTINATION_MSG + ' 目的地を設定してください。')

    # このボタンを押すと未達成セットからランダムでデータを1つ取得して表示する
    next_destination = st.empty()
    if next_destination.button('次の行先を決める'):
        if destination is None or destination == b'':
            next: str = redis_conn.spop('unachieved')
            next = next.decode('utf-8')
            redis_conn.set('destination', next)
            next_station.write(next)
        else:
            st.warning('現在ミッション進行中です' + '先にゴールしてください。')

    # 達成状況を表示
    st.markdown('### 達成状況')

    unachieved_count = st.empty()
    achieved_count = st.empty()

    if st.button('達成状況の確認・更新'):
        unachieved_st_cnt = redis_conn.scard('unachieved')
        achieved_st_cnt = redis_conn.scard('achieved')

        achieved_count.markdown(f'達成済み: {achieved_st_cnt} ')
        unachieved_count.markdown(f'未達成: {unachieved_st_cnt} ')

# メイン処理
if __name__ == '__main__':
    main()
