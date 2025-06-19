import os
import json

def generate_json_from_folders(folder_path):
    # 初始化数据结构
    data = {
        "topics": [],
        "files": {}
    }

    # 遍历指定路径下的所有文件夹
    for folder_name in os.listdir(folder_path):
        folder_path_full = os.path.join(folder_path, folder_name)
        
        # 确保是文件夹
        if os.path.isdir(folder_path_full):
            # 添加专题信息
            topic_id = f"topic{len(data['topics']) + 1}"
            data["topics"].append({
                "id": topic_id,
                "name": folder_name
            })
            
            # 获取文件夹内的文件列表，并去掉文件扩展名
            file_list = [os.path.splitext(f)[0] for f in os.listdir(folder_path_full) if os.path.isfile(os.path.join(folder_path_full, f))]
            data["files"][topic_id] = file_list

    # 将数据写入JSON文件
    with open("topics.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print("JSON文件已生成：topics.json")

# 示例用法
if __name__ == "__main__":
    # 替换为你的文件夹路径
    generate_json_from_folders("./contents/blogs")