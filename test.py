# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk
import subprocess
import sys
import platform
import psutil
import os
import winreg

class RobloxPerformanceOptimizer:
    def __init__(self, master):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.master = master
        master.title("Roblox Performance Optimizer")
        master.geometry("450x500")
        master.resizable(False, False)

        self.main_frame = ctk.CTkFrame(master, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Roblox Performance Optimizer", 
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Sección de rendimiento del sistema
        self.system_frame = ctk.CTkFrame(self.main_frame)
        self.system_frame.pack(padx=20, pady=10, fill="x")

        self.system_label = ctk.CTkLabel(
            self.system_frame, 
            text="Rendimiento del Sistema",
            font=("Arial", 16, "bold")
        )
        self.system_label.pack(pady=(10, 5))

        # Botones de optimización
        self.optimize_buttons = [
            ("Limpiar archivos temporales", self.clean_temp_files),
            ("Ajustar prioridad de procesos", self.optimize_processes),
            ("Optimizar configuración de energia", self.optimize_power_settings)
        ]

        for button_text, command in self.optimize_buttons:
            btn = ctk.CTkButton(
                self.main_frame, 
                text=button_text, 
                command=command,
                corner_radius=6
            )
            btn.pack(pady=5, padx=20, fill="x")

        # Información del sistema
        self.info_label = ctk.CTkLabel(
            self.main_frame, 
            text=self.get_system_info(),
            font=("Arial", 12),
            justify="left"
        )
        self.info_label.pack(pady=10, padx=20)

        # Botón de análisis final
        self.analyze_button = ctk.CTkButton(
            self.main_frame, 
            text="Análisis Completo", 
            command=self.full_system_analysis,
            fg_color="green",
            hover_color="darkgreen"
        )
        self.analyze_button.pack(pady=10, padx=20, fill="x")

    def clean_temp_files(self):
        try:
            # Limpiar archivos temporales de Windows
            temp_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Temp')
            subprocess.run(['cmd', '/c', f'del /q /f /s "{temp_dir}\\*"'], 
                           shell=True, capture_output=True)
            
            # Limpiar archivos temporales de Roblox
            roblox_temp = os.path.join(os.getenv('LOCALAPPDATA'), 'Roblox', 'Temp')
            subprocess.run(['cmd', '/c', f'del /q /f /s "{roblox_temp}\\*"'], 
                           shell=True, capture_output=True)
            
            tk.messagebox.showinfo("Éxito", "Archivos temporales limpiados correctamente")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudieron limpiar archivos: {e}")

    def optimize_processes(self):
        try:
            # Ajustar prioridad de procesos relacionados con juegos
            processes_to_optimize = ['RobloxPlayerBeta.exe', 'RobloxStudio.exe']
            
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] in processes_to_optimize:
                    try:
                        proc.nice(psutil.HIGH_PRIORITY_CLASS)
                    except Exception:
                        pass
            
            tk.messagebox.showinfo("Optimización", "Procesos de Roblox optimizados")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudieron optimizar procesos: {e}")

    def optimize_power_settings(self):
        try:
            # Comando para establecer plan de energía de alto rendimiento
            subprocess.run(['powercfg', '-setactive', 'SCHEME_MIN'], check=True)
            
            tk.messagebox.showinfo("Energía", "Configuración de energía optimizada")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo optimizar energía: {e}")

    def get_system_info(self):
        # Obtener información del sistema
        cpu = platform.processor()
        ram = f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
        os_version = platform.platform()
        
        return f"CPU: {cpu}\nRAM: {ram}\nSistema: {os_version}"

    def full_system_analysis(self):
        # Análisis completo de rendimiento
        analysis_report = []
        
        # Uso de CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        analysis_report.append(f"Uso de CPU: {cpu_percent}%")
        
        # Uso de memoria
        mem = psutil.virtual_memory()
        analysis_report.append(f"Memoria usada: {mem.percent}%")
        
        # Procesos en ejecución
        process_count = len(list(psutil.process_iter()))
        analysis_report.append(f"Procesos en ejecución: {process_count}")
        
        # Mostrar reporte
        report_window = ctk.CTkToplevel(self.master)
        report_window.title("Análisis de Rendimiento")
        report_window.geometry("300x250")
        
        report_label = ctk.CTkLabel(
            report_window, 
            text="\n".join(analysis_report),
            font=("Arial", 14)
        )
        report_label.pack(padx=20, pady=20)

def main():
    root = ctk.CTk()
    performance_optimizer = RobloxPerformanceOptimizer(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        import customtkinter
        import psutil
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter', 'psutil'])
        import customtkinter
        import psutil

    main()
