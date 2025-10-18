import json
import os
import sys
import json
from pyfiglet import Figlet
import pandas as pd

from respond import Respond, TaskMeta

IEXEC_OUT = os.getenv('IEXEC_OUT', './output')

computed_json = {}

try:
    messages = []
    respond = Respond()

    # 通过args获取: 评测任务id，dab评测服务镜像地址，dab评测服务镜像标签, 评测数据集名称
    args = sys.argv[1:]
    print(f"Received {len(args)} args")

    try:
        # 评测任务元数据
        task_meta = TaskMeta(
            task_id=args[0],
            dab_image_address=args[1],
            dab_image_tag=args[2],
            dataset_name=args[3]
        )
        # 通过inputFiles获取评测数据集
        input_dir = os.environ.get('IEXEC_INPUT_FILES_FOLDER', './input')
        print(f"Input directory: {input_dir}")
        
        file_path = os.path.join(input_dir, task_meta.dataset_name)
        print(f"Looking for file at: {file_path}")
        print(f"Input directory: {input_dir}")
        print(f"Directory contents: {os.listdir(input_dir) if os.path.exists(input_dir) else 'Directory does not exist'}")

        df = pd.read_csv(file_path)
        respond.task_meta = task_meta
        respond.dataset_size = df.shape[0]
        # TODO: 执行评测任务和获取评测结果
    except Exception as e:
        print('It seems there is an issue with your protected data:', e)
        respond.error = str(e)

    messages.append(respond.to_json())
    txt = f"Respond from dab worker:\n {' '.join(messages) if len(messages) > 0 else 'No messages'}"

    with open(IEXEC_OUT + '/result.txt', 'w') as f:
        f.write(txt)
    computed_json = {'deterministic-output-path': IEXEC_OUT + '/result.txt'}
except Exception as e:
    print(e)
    computed_json = {'deterministic-output-path': IEXEC_OUT,
                     'error-message': 'Oops something went wrong'}
finally:
    with open(IEXEC_OUT + '/computed.json', 'w') as f:
        json.dump(computed_json, f)
