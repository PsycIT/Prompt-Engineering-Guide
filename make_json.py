import json
import os

def make_json(mk_type, data):
    if not os.path.exists('json'):
        os.mkdir('json')

    fname = os.path.join('json/', mk_type) + '_data.json'
    with open(fname, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
    print('Saved ', fname)

def summary_json(summary_output):
    print('making json... (summary)')
    summary_split = summary_output.split('-')
    summary_split = summary_split[1:]
    print(summary_split)

    json_data_list = []
    for i in range(len(summary_split)):
        json_data_list.append(summary_split[i])

    json_data = {'summary': json_data_list}
    print(json_data)
    make_json('summary', json_data)


def ox_json(ox_output):
    print('making json... (ox quiz)')
    ox_split = ox_output.split('\n')
    # ox_split = ox_split[1:]
    print(ox_split)

    quiz_num = 1
    json_data_list = []
    for i in range(1, len(ox_split), 6):
        quiz_dict = {}

        quiz_dict['no.'] = quiz_num
        quiz_dict['question'] = ox_split[i]
        quiz_dict['answer'] = ox_split[i+2][-1]
        quiz_dict['explanation'] = ox_split[i+3].split(':')[1]

        json_data_list.append(quiz_dict)

        quiz_num += 1

    json_data = {'quizset': json_data_list}
    make_json('ox', json_data)


def kg_json(kg_output):
    print('making json... (kg)')
    graph_dict = {}

    kg_split = kg_output.split('\n\n')
    node_split = kg_split[1].split('\n')
    node_split = node_split[2:]

    node_list = []
    node_dict = {}
    node_id = 1
    for i in range(len(node_split)):
        nodes = node_split[i].split('|')

        if not nodes[1].strip() in node_dict:
            node_dict[nodes[1].strip()] = node_id
            node_id += 1
        if not nodes[2].strip() in node_dict:
            node_dict[nodes[2].strip()] = node_id
            node_id += 1

    print(node_dict)
    for k in node_dict.keys():
        tmp_dict = {}
        tmp_dict['label'] = k
        tmp_dict['id'] = node_dict[k]

        node_list.append(tmp_dict)
    # print(node_list)

    edge_list = []
    for i in range(len(node_split)):
        nodes = node_split[i].split('|')

        tmp_dict = {}
        tmp_dict['from'] = node_dict[nodes[1].strip()]
        tmp_dict['to'] = node_dict[nodes[2].strip()]
        tmp_dict['label'] = nodes[3].strip()

        edge_list.append(tmp_dict)
    # print(edge_list)

    graph_dict['graph'] = {'nodes': node_list, 'edges': edge_list}
    # print(graph_dict)

    json_data = graph_dict
    make_json('kg', json_data)


data = """첫 번째 테이블은 다음과 같이 구성됩니다:

| source | target | relation |
|--------|--------|----------|
| 생산   | 마스크 | 생산     |
| 생산   | 옷     | 생산     |
| 생산   | 귀걸이 | 생산     |
| 생산   | 자동차 | 생산     |
| 생산   | 드라마 | 생산     |
| 생산   | 인강   | 생산     |
| 생산   | 공연   | 생산     |
| 생산   | 진료   | 생산     |

두 번째 테이블은 다음과 같이 구성됩니다:

| term name | term definition |
|-----------|----------------|
| 경제활동  | 경제적인 활동 또는 행위 |
| 생산      | 자원을 이용하여 상품이나 서비스를 만들어내는 과정 |
| 분배      | 생산된 상품이나 서비스를 사람들에게 나누어주는 과정 |
| 소비      | 생산된 상품이나 서비스를 사람들이 사용하거나 소비하는 과정 |
| 주체      | 경제활동을 수행하는 주체 |
| 희소성    | 자원이 한정되어 있어 모든 욕구를 충족시키기 어려운 상태 |
| 경제 문제 | 경제적인 측면에서 발생하는 문제 또는 고민 |
| 마스크    | 호흡기 보호를 위해 사용되는 물품 |
| 옷        | 사람들이 입는 의류 |
| 귀걸이    | 귀에 착용하는 장신구 |
| 자동차    | 사람들이 이동 수단으로 사용하는 차량 |
| 드라마    | 연기자들이 연기를 통해 이야기를 전달하는 작품 |
| 인강      | 인터넷을 통해 제공되는 교육 강의 |
| 공연      | 예술가들이 공연을 통해 작품을 선보이는 행위 |
| 진료      | 의사가 환자를 진찰하고 치료하는 행위 |
"""


# summary_json(data)
# ox_json(data)
# kg_json(data)
# print(data)