# Importa a função de scraping do outro arquivo
from scraper import coletar_manchetes_g1 

# Importa as bibliotecas da interface e de suporte
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import webbrowser

class ColetorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coletor de Notícias - G1")
        self.root.geometry("800x600")

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10))
        style.configure("TLabel", font=("Segoe UI", 9))
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.buscar_btn = ttk.Button(self.frame, text="Buscar Últimas Notícias", command=self.iniciar_busca)
        self.buscar_btn.pack(fill=tk.X, pady=5)

        self.text_area = tk.Text(self.frame, wrap=tk.WORD, font=("Segoe UI", 12), relief=tk.SOLID, borderwidth=1)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.text_area, orient=tk.VERTICAL, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        
        self.text_area.tag_configure("link", foreground="blue", underline=True)
        self.text_area.tag_bind("link", "<Enter>", self._on_link_enter)
        self.text_area.tag_bind("link", "<Leave>", self._on_link_leave)

        self.status_label = ttk.Label(self.frame, text="Pronto para buscar.")
        self.status_label.pack(side=tk.LEFT, pady=5)

    def _on_link_enter(self, event):
        self.text_area.config(cursor="hand2")

    def _on_link_leave(self, event):
        self.text_area.config(cursor="")

    def _open_url(self, url):
        webbrowser.open_new_tab(url)

    def iniciar_busca(self):
        self.buscar_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Buscando notícias, por favor aguarde...")
        
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete("1.0", tk.END)
        self.text_area.config(state=tk.DISABLED)

        thread = threading.Thread(target=self.executar_busca)
        thread.start()

    def executar_busca(self):
        # Aqui chamamos a função importada do arquivo scraper.py
        resultado = coletar_manchetes_g1()
        self.root.after(0, self.atualizar_interface, resultado)

    def atualizar_interface(self, resultado):
        self.text_area.config(state=tk.NORMAL)

        if isinstance(resultado, list):
            for index, noticia in enumerate(resultado):
                titulo = noticia['titulo']
                link = noticia['link']

                self.text_area.insert(tk.END, f"{index + 1}. {titulo}\n", ("titulo",))
                link_text = "     [Abrir Notícia]\n\n"
                link_tag = f"link-{index}"
                self.text_area.insert(tk.END, link_text, ("link", link_tag))
                self.text_area.tag_bind(link_tag, "<Button-1>", lambda e, url=link: self._open_url(url))

            self.status_label.config(text=f"Pronto! {len(resultado)} notícias carregadas.")
        else:
            messagebox.showerror("Erro", resultado)
            self.status_label.config(text="Ocorreu um erro ao buscar as notícias.")
        
        self.text_area.config(state=tk.DISABLED)
        self.buscar_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColetorApp(root)
    root.mainloop()
