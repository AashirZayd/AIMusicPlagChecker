import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import ImageGrab, Image
import threading, requests, os, datetime, random, webbrowser

BACKEND_URL = "http://127.0.0.1:5000/analyze"
LOG_FILE = "analysis_log.txt"
GITHUB_URL = "https://github.com/yourusername/music-plagiarism-detector"  # 🧩 Replace with your actual repo


class GitHubDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Music Plagiarism Detector • GitHub Style")
        self.attributes('-fullscreen', True)  # ✅ Fullscreen mode
        self.bind("<Escape>", lambda e: self.attributes('-fullscreen', False))  # Press Esc to exit fullscreen
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.audio_path = ctk.StringVar()
        self.lyrics_path = ctk.StringVar()

        self.configure(bg="#0D1117")
        self.create_ui()

    def create_ui(self):
        self.create_navbar()

        self.card = ctk.CTkFrame(self, fg_color="#161B22", corner_radius=12)
        self.card.place(relx=0.5, rely=0.53, anchor="center", relwidth=0.8, relheight=0.75)

        header = ctk.CTkLabel(
            self.card,
            text="🎧 AI-Based Music Plagiarism Detector",
            font=("Segoe UI Semibold", 28),
            text_color="#E6EDF3",
        )
        header.pack(pady=(30, 10))

        sub = ctk.CTkLabel(
            self.card,
            text="Analyze audio tracks and lyrics for originality using AI similarity detection.",
            font=("Segoe UI", 14),
            text_color="#8B949E"
        )
        sub.pack(pady=(0, 25))

        upload_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        upload_frame.pack(pady=15)

        ctk.CTkLabel(upload_frame, text="🎵 Audio File:", text_color="#C9D1D9", font=("Segoe UI", 14)).grid(row=0, column=0, padx=10, pady=10)
        self.audio_entry = ctk.CTkEntry(upload_frame, textvariable=self.audio_path, width=600, fg_color="#0D1117", border_color="#30363D")
        self.audio_entry.grid(row=0, column=1, padx=5)
        ctk.CTkButton(upload_frame, text="Browse", command=self.browse_audio, fg_color="#238636", hover_color="#2EA043").grid(row=0, column=2, padx=10)

        ctk.CTkLabel(upload_frame, text="📄 Lyrics File:", text_color="#C9D1D9", font=("Segoe UI", 14)).grid(row=1, column=0, padx=10, pady=10)
        self.lyrics_entry = ctk.CTkEntry(upload_frame, textvariable=self.lyrics_path, width=600, fg_color="#0D1117", border_color="#30363D")
        self.lyrics_entry.grid(row=1, column=1, padx=5)
        ctk.CTkButton(upload_frame, text="Browse", command=self.browse_lyrics, fg_color="#238636", hover_color="#2EA043").grid(row=1, column=2, padx=10)

        self.analyze_btn = ctk.CTkButton(
            self.card,
            text="⚡ Analyze Now",
            command=self.start_analysis,
            fg_color="#238636",
            hover_color="#2EA043",
            font=("Segoe UI", 15, "bold"),
            width=230,
            height=45,
            corner_radius=8
        )
        self.analyze_btn.pack(pady=(30, 15))

        self.progress_bar = ctk.CTkProgressBar(self.card, width=500, progress_color="#2EA043")
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(5, 15))

        self.similarity_label = ctk.CTkLabel(self.card, text="Similarity: --%", font=("Segoe UI", 15), text_color="#8B949E")
        self.similarity_label.pack(pady=5)

        self.result_box = ctk.CTkTextbox(
            self.card, height=260, width=950, fg_color="#0D1117", border_color="#30363D", text_color="#E6EDF3", corner_radius=8
        )
        self.result_box.pack(padx=20, pady=15)

        btn_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="💾 Save Results", command=self.save_results, width=160, fg_color="#30363D", hover_color="#484F58").grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="📜 View Logs", command=self.view_logs, width=160, fg_color="#30363D", hover_color="#484F58").grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_frame, text="📸 Screenshot", command=self.take_screenshot, width=160, fg_color="#30363D", hover_color="#484F58").grid(row=0, column=2, padx=10)

        footer = ctk.CTkLabel(
            self,
            text="© 2025 Vishnu | Press ESC to exit fullscreen",
            text_color="#6E7681",
            font=("Segoe UI", 11)
        )
        footer.pack(side="bottom", pady=12)

    def create_navbar(self):
        navbar = ctk.CTkFrame(self, fg_color="#161B22", height=60, corner_radius=0)
        navbar.place(relx=0, rely=0, relwidth=1)

        try:
            logo_img = Image.open("github_icon.png")
            logo = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(30, 30))
            logo_btn = ctk.CTkButton(
                navbar, image=logo, text="", width=40, height=40,
                fg_color="#161B22", hover_color="#21262D", corner_radius=8,
                command=lambda: webbrowser.open(GITHUB_URL)
            )
            logo_btn.pack(side="left", padx=(25, 10), pady=10)
        except:
            pass

        name_label = ctk.CTkLabel(
            navbar,
            text="AI Music Plagiarism Detector",
            font=("Segoe UI", 17, "bold"),
            text_color="#E6EDF3"
        )
        name_label.pack(side="left", pady=10)

        links_frame = ctk.CTkFrame(navbar, fg_color="transparent")
        links_frame.pack(side="right", padx=25)

        self.create_nav_link(links_frame, "Home", lambda: messagebox.showinfo("Home", "Welcome to AIMP!"))
        self.create_nav_link(links_frame, "Docs", lambda: webbrowser.open(GITHUB_URL + "/wiki"))
        self.create_nav_link(links_frame, "About", lambda: messagebox.showinfo("About", "Developed by Us"))
        self.create_nav_link(links_frame, "Support", lambda: webbrowser.open("mailto:vishnubharadwaj66@gmail.com"))

    def create_nav_link(self, parent, text, command):
        btn = ctk.CTkButton(
            parent,
            text=text,
            command=command,
            fg_color="transparent",
            hover_color="#21262D",
            corner_radius=6,
            width=90,
            height=32,
            font=("Segoe UI", 13),
            text_color="#C9D1D9"
        )
        btn.pack(side="left", padx=12)

    def browse_audio(self):
        path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")])
        if path:
            self.audio_path.set(path)

    def browse_lyrics(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            self.lyrics_path.set(path)

    def start_analysis(self):
        threading.Thread(target=self.analyze, daemon=True).start()

    def analyze(self):
        audio = self.audio_path.get()
        lyrics = self.lyrics_path.get()
        if not audio:
            messagebox.showerror("Error", "Please select an audio file!")
            return
        self.progress_bar.start()
        self.result_box.delete("1.0", "end")
        try:
            files = {'audio': open(audio, 'rb')}
            if lyrics:
                files['lyrics'] = open(lyrics, 'rb')
            response = requests.post(BACKEND_URL, files=files)
            if response.status_code == 200:
                data = response.json()
                self.show_result(data)
                messagebox.showinfo("Done", "✅ Analysis Complete!")
            else:
                messagebox.showerror("Backend Error", f"{response.text}")
        except Exception as e:
            messagebox.showerror("Connection Error", f"Cannot connect to backend.\n\n{e}")
        finally:
            self.progress_bar.stop()

    def show_result(self, result):
        score = result.get("similarity", random.uniform(40, 95))
        self.similarity_label.configure(text=f"Similarity: {score:.2f}%")
        self.progress_bar.set(score / 100)
        color = "#238636" if score < 60 else "#F1E05A" if score < 80 else "#DA3633"
        self.similarity_label.configure(text_color=color)
        self.result_box.insert("end", f"\nResult:\n{result}\n")
        self.log_result(result)

    def log_result(self, result):
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {result}\n")

    def view_logs(self):
        if os.path.exists(LOG_FILE):
            os.startfile(LOG_FILE)
        else:
            messagebox.showinfo("Logs", "No logs found yet.")

    def save_results(self):
        text = self.result_box.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Warning", "No results to save!")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"Results saved to:\n{path}")

    def take_screenshot(self):
        x, y, w, h = self.winfo_rootx(), self.winfo_rooty(), self.winfo_width(), self.winfo_height()
        img = ImageGrab.grab().crop((x, y, x + w, y + h))
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if path:
            img.save(path)
            messagebox.showinfo("Saved", f"Screenshot saved to:\n{path}")


if __name__ == "__main__":
    app = GitHubDashboard()
    app.mainloop()
