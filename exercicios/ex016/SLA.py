import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

# Configurações iniciais
ctk.set_appearance_mode("System")  # Light ou Dark
ctk.set_default_color_theme("blue")


class ProjetoFrame(ctk.CTkFrame):
    def __init__(self, master, titulo, descricao, tecnologias, imagem_url, link, **kwargs):
        super().__init__(master, **kwargs)

        # Baixar imagem
        try:
            response = requests.get(imagem_url)
            imagem_pil = Image.open(BytesIO(response.content)).resize((300, 180))
            self.imagem = ctk.CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(300, 180))
            self.imagem_label = ctk.CTkLabel(self, image=self.imagem, text="")
            self.imagem_label.pack(pady=10)
        except:
            print(f"Erro ao carregar imagem de {imagem_url}")

        self.titulo_label = ctk.CTkLabel(self, text=titulo, font=("Arial", 18, "bold"))
        self.titulo_label.pack(pady=(5, 0))

        self.descricao_label = ctk.CTkLabel(self, text=descricao, font=("Arial", 14), wraplength=400, justify="center")
        self.descricao_label.pack(pady=(5, 0))

        self.tecnologias_label = ctk.CTkLabel(self, text="Tecnologias: " + ", ".join(tecnologias), font=("Arial", 12, "italic"))
        self.tecnologias_label.pack(pady=(5, 10))

        self.link_button = ctk.CTkButton(self, text="Ver Projeto", command=lambda: webbrowser.open(link))
        self.link_button.pack(pady=(0, 10))


class PortifolioApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Portfólio - Ediley Matos")
        self.geometry("700x800")

        self.nome_label = ctk.CTkLabel(self, text="Ediley Matos", font=("Arial", 28, "bold"))
        self.nome_label.pack(pady=(20, 5))

        self.profissao_label = ctk.CTkLabel(self, text="Desenvolvedor Full Stack", font=("Arial", 20))
        self.profissao_label.pack(pady=(0, 20))

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=600, height=600)
        self.scrollable_frame.pack(pady=10, padx=20)

        # Adicionar projetos
        self.adicionar_projeto(
            "Sistema de Gestão de Estoque",
            "Aplicação web para gerenciar estoque de empresas.",
            ["Python", "Flask", "MySQL"],
            "https://images.unsplash.com/photo-1605379399642-870262d3d051?fit=crop&w=600&q=80",  # Imagem de estoque
            "https://www.seuprojeto1.com"  # Link exemplo
        )

        self.adicionar_projeto(
            "Site de Portfólio",
            "Site pessoal para apresentar projetos e blog.",
            ["HTML", "CSS", "JavaScript"],
            "https://images.unsplash.com/photo-1581090700227-1c065c1d25b4?fit=crop&w=600&q=80",  # Imagem de site
            "https://www.seuportifolio.com"  # Link exemplo
        )

        self.adicionar_projeto(
            "App de Controle Financeiro",
            "Aplicativo mobile para controle de despesas pessoais.",
            ["Python", "Kivy"],
            "https://images.unsplash.com/photo-1600267185789-c3d0677f57c9?fit=crop&w=600&q=80",  # Imagem de app
            "https://www.seuappfinanceiro.com"  # Link exemplo
        )

    def adicionar_projeto(self, titulo, descricao, tecnologias, imagem_url, link):
        projeto_frame = ProjetoFrame(self.scrollable_frame, titulo, descricao, tecnologias, imagem_url, link)
        projeto_frame.pack(pady=15, fill="x", padx=10)


if __name__ == "__main__":
    app = PortifolioApp()
    app.mainloop()
