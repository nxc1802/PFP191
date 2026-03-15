def count_sentences_with_keyword(filepath, keyword):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        sentences = []
        for part in text.replace("!", ".").replace("?", ".").split("."):
            sentences.append(part)
        count = sum(1 for s in sentences if keyword.lower() in s.lower())
        return count

print(count_sentences_with_keyword("Giải đề/PFP191 - PE - FA23/Bài giải/Vietnamese_Declaration_of_Independence.txt", "independence"))

def top_10_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        text_clean = ''
        for char in text:
            if char.isalnum() or char.isspace():
                text_clean += char
        words = text_clean.lower().split()
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_counts[:10]

def word_frequency(filepath):
    freq = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            
        # Loại bỏ các dấu câu cơ bản bằng cách thay thế thành khoảng trắng
        for p in ".,?!;:\"'()[]{}":
            text = text.replace(p, " ")
            
        words = text.lower().split()
        
        # Đếm tần suất xuất hiện của từng từ
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        
    return freq

top_10_words_list = top_10_words("Giải đề/PFP191 - PE - FA23/Bài giải/Vietnamese_Declaration_of_Independence.txt")
for i in top_10_words_list:
    print(i[0], i[1])