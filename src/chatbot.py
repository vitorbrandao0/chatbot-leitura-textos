from src.rag_pipeline import answer_question

def chatbot():
    print("Chatbot (Examinador de PDFs): Pergunte algo sobre o conteúdo do PDF.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit"]:
            print("Encerrando o chatbot.")
            break
        response = answer_question(user_input)
        print(f"Chatbot: {response}")