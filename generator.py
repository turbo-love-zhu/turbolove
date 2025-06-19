import os
import json

def generate_json_from_folders(folder_path):
    # 初始化数据结构
    data = {
        "topics": [],
        "files": {}
    }

    # 获取指定路径下的所有文件夹名称，并按照数字排序
    folder_names = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    sorted_folder_names = sorted(folder_names, key=lambda x: int(x.split('.')[0]))

    # 遍历排序后的文件夹
    for folder_name in sorted_folder_names:
        folder_path_full = os.path.join(folder_path, folder_name)
        
        # 添加专题信息
        topic_id = f"topic{len(data['topics']) + 1}"
        data["topics"].append({
            "id": topic_id,
            "name": folder_name
        })
        
        # 获取文件夹内的文件列表
        file_list = [f for f in os.listdir(folder_path_full) if os.path.isfile(os.path.join(folder_path_full, f))]
        
        # 按文件名前的数字排序
        sorted_file_list = sorted(file_list, key=lambda x: int(os.path.splitext(x)[0].split('.')[0]))
        
        # 去掉文件扩展名
        sorted_file_list = [os.path.splitext(f)[0] for f in sorted_file_list]
        
        data["files"][topic_id] = sorted_file_list

    # 将数据写入JSON文件
    with open("topics.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print("JSON文件已生成：topics.json")

# 示例用法
if __name__ == "__main__":
    # 替换为你的文件夹路径
    generate_json_from_folders("./contents/blogs")