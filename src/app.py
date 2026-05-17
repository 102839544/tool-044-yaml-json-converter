#!/usr/bin/env python3
"""
YAML与JSON互转工具
"""
import sys, json, tkinter as tk
from tkinter import messagebox, scrolledtext
import tkinter as tk

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

class App:
    def __init__(self, root):
        self.root = root
        root.title("YAML/JSON互转工具 v1.0")
        root.geometry("800x600")
        self.build_ui()
    
    def build_ui(self):
        f = tk.Frame(self.root, bg="#00897b", height=50)
        f.pack(fill="x")
        tk.Label(f, text="🔄 YAML ↔ JSON", font=("Arial",14,"bold"),
                 fg="white", bg="#00897b").pack(pady=12)
        
        main = tk.Frame(self.root, padx=15, pady=10)
        main.pack(fill="both", expand=True)
        
        bf = tk.Frame(main)
        bf.pack(fill="x", pady=5)
        tk.Button(bf, text="YAML → JSON", command=self.yaml_to_json,
                  bg="#00897b", fg="white", padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="JSON → YAML", command=self.json_to_yaml,
                  bg="#00897b", fg="white", padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="复制结果", command=self.copy_result,
                  padx=15).pack(side="left", padx=10)
        tk.Button(bf, text="清空", command=self.clear,
                  bg="#d9534f", fg="white", padx=15).pack(side="right", padx=5)
        
        tk.Label(main, text="输入：", font=("Arial",10,"bold")).pack(anchor="w")
        self.input_txt = scrolledtext.ScrolledText(main, font=("Consolas",10), height=10)
        self.input_txt.pack(fill="x", pady=5)
        
        tk.Label(main, text="输出：", font=("Arial",10,"bold")).pack(anchor="w", pady=(10,0))
        self.output_txt = scrolledtext.ScrolledText(main, font=("Consolas",10),
                                                      height=10, bg="#e0f2f1")
        self.output_txt.pack(fill="x", pady=5)
        
        self.status = tk.Label(main, text="粘贴YAML或JSON后点击转换",
                               font=("Arial",10), fg="gray")
        self.status.pack()
    
    def yaml_to_json(self):
        if not HAS_YAML:
            messagebox.showerror("缺少依赖", "请运行：pip install pyyaml")
            return
        try:
            data = yaml.safe_load(self.input_txt.get(1.0, "end"))
            result = json.dumps(data, indent=2, ensure_ascii=False)
            self.output_txt.delete(1.0, "end")
            self.output_txt.insert(1.0, result)
            self.status.config(text="✅ YAML → JSON 转换成功")
        except Exception as e:
            messagebox.showerror("错误", str(e))
    
    def json_to_yaml(self):
        if not HAS_YAML:
            messagebox.showerror("缺少依赖", "请运行：pip install pyyaml")
            return
        try:
            data = json.loads(self.input_txt.get(1.0, "end"))
            result = yaml.dump(data, allow_unicode=True, default_flow_style=False)
            self.output_txt.delete(1.0, "end")
            self.output_txt.insert(1.0, result)
            self.status.config(text="✅ JSON → YAML 转换成功")
        except Exception as e:
            messagebox.showerror("错误", str(e))
    
    def copy_result(self):
        text = self.output_txt.get(1.0, "end")
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("复制成功", "结果已复制到剪贴板")
    
    def clear(self):
        self.input_txt.delete(1.0, "end")
        self.output_txt.delete(1.0, "end")
        self.status.config(text="已清空")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
