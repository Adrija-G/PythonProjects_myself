from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalnum()]
    print(tokens)
    return tokens
    
def contains_query(sentence_tokens, queries):
    for token in sentence_tokens:
        if any(query == token for query in queries):
            return True
    return False

def highlight_relevant_parts(document, queries):
    stop_words = set(stopwords.words('english'))
    
    highlighted_document = ""
    for i, sentence in enumerate(sent_tokenize(document)):
        sentence_tokens = preprocess_text(sentence)
        sentence_tokens = [token for token in sentence_tokens if token not in stop_words]
        
        if contains_query(sentence_tokens, queries):
            ln_val = i + 1  # Line number
            highlighted_sentence = []
            for token in sentence_tokens:
                if any(query in token for query in queries):
                    highlighted_token = f'\033[1m{token}\033[0m'
                else:
                    highlighted_token = token
                highlighted_sentence.append(highlighted_token)
            highlighted_document += f"Line {ln_val}: {' '.join(highlighted_sentence)}\n"

    return highlighted_document

queries = []
num_queries = int(input("Enter the number of keywords to be searched: "))
for _ in range(num_queries):
    query = input("Enter keyword(s): ").lower()
    queries.append(query)

document = input('Enter text input:\n')

highlighted_doc = highlight_relevant_parts(document, queries)
print(highlighted_doc)
