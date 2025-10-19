import json
import os
import sys
import json
from pyfiglet import Figlet
import pandas as pd
from loguru import logger

from respond import Respond, TaskMeta

IEXEC_OUT = os.getenv('IEXEC_OUT', '/iexec_out')
IEXEC_IN = os.getenv('IEXEC_IN', '/iexec_in')

computed_json = {}

try:
    messages = []
    respond = Respond()

    # 通过args获取: 评测任务id，dab评测服务镜像地址，dab评测服务镜像标签, 评测数据集名称
    args = sys.argv[1:]
    print(f"Received {len(args)} args")

    try:
        # if len(args) < 4:
        #     print(f"ERROR: Not enough arguments. Expected 4, got {len(args)}")
        #     respond.error = f"Not enough arguments. Expected 4, got {len(args)}"
        # 评测任务元数据
        task_meta = TaskMeta(
            task_id=args[0],
            dab_image_address=args[1],
            dab_image_tag=args[2],
            dataset_name=args[3]
        )
        respond.task_meta = task_meta
        # 通过inputFiles获取评测数据集
        logger.info(f"Input directory: {IEXEC_IN}")
        logger.info(f"Directory contents: {os.listdir(IEXEC_IN) if os.path.exists(IEXEC_IN) else 'Directory does not exist'}")
        
        file_path = os.path.join(IEXEC_IN, task_meta.dataset_name)
        if os.path.exists(file_path):
            logger.info(f"File found at: {file_path}")
        else:
            logger.warning(f"File not found at: {file_path}, using first file: {file_path}")
            file_name = os.listdir(IEXEC_IN)[0]
            file_path = os.path.join(IEXEC_IN, file_name)
            logger.info(f"Using first file: {file_path}")
            respond.task_meta.dataset_name = file_name
        df = pd.read_csv(file_path)
        respond.dataset_size = df.shape[0]
        # 拉取镜像
        # TODO: 执行评测任务和获取评测结果
    except Exception as e:
        e = str(e) + f"Directory contents: {os.listdir(IEXEC_IN) if os.path.exists(IEXEC_IN) else 'Directory does not exist'}"
        logger.error('It seems there is an issue with your input file:', e)
        respond.error = str(e)

    messages.append(respond.to_json())
    txt = f"Respond from dab worker:\n {' '.join(messages) if len(messages) > 0 else 'No messages'}"

    with open(IEXEC_OUT + '/result.txt', 'w') as f:
        f.write(txt)
    computed_json = {'deterministic-output-path': IEXEC_OUT + '/result.txt'}
except Exception as e:
    logger.error(e)
    computed_json = {'deterministic-output-path': IEXEC_OUT,
                     'error-message': 'Oops something went wrong'}
finally:
    with open(IEXEC_OUT + '/computed.json', 'w') as f:
        json.dump(computed_json, f)
