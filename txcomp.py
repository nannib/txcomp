import string
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def get_word_frequencies(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stopwords.words('italian')]
    word_frequencies = FreqDist(filtered_words)
    return word_frequencies

def clear_text(text_widget):
    text_widget.delete("1.0", "end")

def compare_styles():
    text1 = text1_entry.get("1.0", "end-1c")
    text2 = text2_entry.get("1.0", "end-1c")

    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    freq1 = get_word_frequencies(text1)
    freq2 = get_word_frequencies(text2)

    # Calcola la similarità tra i due testi utilizzando la cosine similarity
    common_words = set(freq1) & set(freq2)
    numerator = sum(freq1[word] * freq2[word] for word in common_words)
    sum1 = sum(freq1[word] ** 2 for word in freq1)
    sum2 = sum(freq2[word] ** 2 for word in freq2)
    denominator = (sum1 * sum2) ** 0.5

    if denominator == 0:
        similarity = 0
    else:
        similarity = (numerator / denominator) * 100

    similarity_label.config(text=f"Similarità tra i due testi: {similarity:.2f}%")

# Creazione della GUI
root = Tk()
root.title("Confronto di Stili di Scrittura V 1.0 - by Nanni Bassetti")
root.geometry("1025x768")

# Ottieni le dimensioni dello schermo
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcola le coordinate per centrare la finestra
x = (screen_width - 1025) // 2  # 1025 è la larghezza della finestra
y = (screen_height - 768) // 2  # 768 è l'altezza della finestra

# Imposta la posizione della finestra al centro dello schermo
root.geometry(f"1025x768+{x}+{y}")

text1_label = Label(root, text="Incolla il testo 1:")
text1_label.pack()

text1_frame = Frame(root)
text1_frame.pack()

text1_entry = ScrolledText(text1_frame, height=20, width=80)
text1_entry.pack(side=LEFT)

clear_button1 = Button(text1_frame, text="Cancella", command=lambda: clear_text(text1_entry))
clear_button1.pack(side=RIGHT)

text2_label = Label(root, text="Incolla il testo 2:")
text2_label.pack()

text2_frame = Frame(root)
text2_frame.pack()

text2_entry = ScrolledText(text2_frame, height=20, width=80)
text2_entry.pack(side=LEFT)

clear_button2 = Button(text2_frame, text="Cancella", command=lambda: clear_text(text2_entry))
clear_button2.pack(side=RIGHT)

compare_button = Button(root, text="Confronta Stili", command=compare_styles)
compare_button.pack()

similarity_label = Label(root, text="")
similarity_label.pack()

root.mainloop()

