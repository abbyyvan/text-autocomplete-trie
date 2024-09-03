#main.py test the functionality
from autocomplete import AutoCompleteSystem

def main():
    ac_system = AutoCompleteSystem()
    words = ["apple", "app", "apricot", "bat", "ball", "cat"]
    
    for word in words:
        ac_system.add_word(word)  # 向系统中添加单词
    
    prefix = input("Enter a prefix to autocomplete: ")  # 输入前缀
    suggestions = ac_system.get_suggestions(prefix)  # 获取建议
    print(f"Suggestions for '{prefix}': {suggestions}")  # 输出建议

if __name__ == "__main__":
    main()
