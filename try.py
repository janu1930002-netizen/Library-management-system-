from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
Builder.load_file("try.kv")
from kivy.uix.scrollview import ScrollView
import sqlite3
conn = sqlite3.connect("LibraryManagementSystem.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
Studentname varchar(50),
student_Id INTEGER PRIMARY KEY,
Program varchar(50),
Faculity varchar(50),
Batch int,
Level varchar(50),
Mobile_no int,
Email varchar(100),
Date_brith varchar(20),
Gender varchar(20),
Status varchar(25),
Maxbooktake int,
Noofbooktake int,
Father_name varchar(30)
)
""")
conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Book(
Bookname varchar(50),
Book_Id INTEGER PRIMARY KEY,
Author_name varchar(50),
Edition int,
Language varchar(50),
Pubilication_year int,
Pubilcation_name varchar(100),
Book_no int,
No_of_taken int,
No_of_book_aviable int,
Accession_no int,
Book_price float,
classification_no int,
Source varchar(50)
)
""")
conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
User varchar(50),
Password varchar(20)
)
""")
try:
    cursor.execute("INSERT INTO User VALUES (?,?)",("Ramkumar","2580"))
except:
    print("worng")
conn.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS LBT(
    Bookname varchar(50),
    Book_id int,
    Student_name varchar(50),
    student_Id int,
    Issue_date varchar(20),
    com varchar(20) PRIMARY KEY,
    FOREIGN KEY(student_Id) REFERENCES Students(student_Id),
    FOREIGN KEY(Book_id) REFERENCES Books(Book_id)
    )""")
conn.commit()
class Slist(Screen):
    pass
class Openingtitle(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_screen,10)

    def switch_screen(self, dt):
        self.manager.current = "logn"

class ListDel(Screen):
    pass
class Listup(Screen):
    pass
class Blist(Screen):
    pass
class BTSlist(Screen):
    pass
class Listdetials(BoxLayout):
    pass
class Booktakenstudentlist(BoxLayout):   
    def bcheck(self,instance):
        self.ids.header.opacity=1
        self.ids.show.disabled=True
        self.ids.header.disabled=False
        self.scroll=ScrollView(do_scroll_x=False,do_scroll_y=True,bar_width=10)
        self.a=GridLayout(cols=6,size_hint_y=None,
            pos_hint= {'center_x':0.5,'center_y':0.5},spacing=40,padding=10)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LBT")
        row = cursor.fetchall()
        for bh in range(len(row)):
            self.a.add_widget(Label(text=str((bh+1)),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][0],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][1]),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][2],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][3]),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][4],bold=True,font_size=30,color=(0,0,0,1)))
        self.a.bind(minimum_height=self.a.setter('height'))
        self.scroll.add_widget(self.a)
        self.add_widget(self.scroll)                                
class Booklist(BoxLayout): 
    a=GridLayout(cols=5,size_hint_y=None,
            pos_hint= {'center_x':0.5,'center_y':0.5},spacing=40,padding=10)  
    def bcheck(self,instance):
        self.remove_widget(self.a)
        self.ids.header.opacity=1
        self.ids.show.disabled=True
        self.ids.header.disabled=False
        self.scroll=ScrollView(do_scroll_x=False,do_scroll_y=True,bar_width=10)
        self.a=GridLayout(cols=5,size_hint_y=None,
            pos_hint= {'center_x':0.5,'center_y':0.5},spacing=40,padding=10)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Book")
        row = cursor.fetchall()
        for bh in range(len(row)):
            self.a.add_widget(Label(text=str((bh+1)),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][0],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][1]),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][6],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][3]),bold=True,font_size=30,color=(0,0,0,1)))
        self.a.bind(minimum_height=self.a.setter('height'))
        self.scroll.add_widget(self.a)
        self.add_widget(self.scroll)
    def back(self,instance):
        self.remove_widget(self.a)
        self.ids.header.opacity=0
        self.ids.show.disabled=True 
        self.ids.header.disabled=False
 
class Studentlist(BoxLayout):
    a=GridLayout(cols=5,size_hint_y=None,
            pos_hint= {'center_x':0.5,'center_y':0.5},spacing=40,padding=10) 
    def bcheck(self,instance):
        self.ids.show.disabled=True
        self.ids.header.opacity=1
        self.ids.header.disabled=False
        self.scroll=ScrollView(do_scroll_x=False,do_scroll_y=True,bar_width=10)
        self.a=GridLayout(cols=5,size_hint_y=None,
            pos_hint= {'center_x':0.5,'center_y':0.5},spacing=40,padding=10)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student ")
        row = cursor.fetchall()
        for bh in range(len(row)):
            self.a.add_widget(Label(text=str((bh+1)),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][0],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][1]),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=row[bh][2],bold=True,font_size=30,color=(0,0,0,1)))
            self.a.add_widget(Label(text=str(row[bh][6]),bold=True,font_size=30,color=(0,0,0,1)))
            self.a.bind(minimum_height=self.a.setter('height'))
        self.scroll.add_widget(self.a)
        self.add_widget(self.scroll)        
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.header.disabled=True
        self.ids.show.disabled=True  
 
 
               
class StudentRed(Screen):
    pass
class BookRed(Screen):
    pass
class BookRedname(Screen):
    pass
class StudentUp(Screen):
    pass
class BookDel(Screen):
    pass
class StudentDel(Screen):
    pass
class BookUp(Screen):
    pass
class Bookreadname(BoxLayout):
    def bcheck(self,instance):
        try:
            self.ids.l.text=""
            t=self.ids.bookcheck.text.upper()
            self.ids.header.opacity=1
            self.ids.header.disabled=False
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book")
            rows= cursor.fetchall()
            t1="Book_Name\t\t\t\tBook_Id\t\t\tBook_Edition\n"
            for row in rows:
                if t in row[0]:
                    t1=t1+row[0]+"\t\t\t\t"+str(row[1])+"\t\t\t"+str(row[3])+"\n"
                    self.ids.l.text=t1
            
        except Exception as e:
            print(e)
            popup = Popup(title="Message",content=Label(text="Book_id is not Found"),size_hint=(None, None),size=(400, 400))
            popup.open() 
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.l.text=""
        self.ids.header.disabled=True
        self.ids.bookcheck.text=""
class Bookread(BoxLayout):
    def bcheck(self,instance):
        try:
            t=self.ids.bookcheck.text
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id="+t)
            row = cursor.fetchone()
            self.ids.name.text=row[0]
            self.ids.bid.text=str(row[1])
            self.ids.aname.text=row[2]
            self.ids.e.text=str(row[3])
            self.ids.lan.text=row[4]
            self.ids.py.text=str(row[5])
            self.ids.pname.text=row[6]
            self.ids.bno.text=str(row[7])
            self.ids.nbt.text=str(row[8])
            self.ids.bna.text=str(row[9])
            self.ids.an.text=str(row[10])
            self.ids.bpri.text=str(row[11])
            self.ids.bcn.text=str(row[12])
            self.ids.sr.text=row[13]
            self.ids.bookcheck.text=""
        except Exception as e:
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
            self.ids.bookcheck.text=""
            popup = Popup(title="Message",content=Label(text="Book_id is not Found"),size_hint=(None, None),size=(400, 400))
            popup.open() 
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
        self.ids.bookcheck.text=""       
class Studentread(BoxLayout):
    def check(self,instance):
        try: 
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE student_Id ="+(self.ids.stidcheck.text))
            row = cursor.fetchone()
            self.ids.name.text=row[0]
            self.ids.stid.text=str(row[1])
            self.ids.program.text=row[2]
            self.ids.faculity.text=row[3]
            self.ids.batch.text=str(row[4])
            self.ids.slevel.text=row[5]
            self.ids.mbno.text=str(row[6])
            self.ids.email.text=row[7]
            self.ids.dob.text=row[8]
            self.ids.sex.text=row[9]
            self.ids.status.text=row[10]
            self.ids.mnbt.text=str(row[11])
            self.ids.nbt.text=str(row[12])
            self.ids.fname.text=row[13]
            self.ids.stidcheck.text=""  
        except Exception as e:
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled:True
            self.ids.stidcheck.text=""
            popup = Popup(title="Message",content=Label(text="Student_id is not Match"),size_hint=(None, None),size=(400, 400))
            popup.open() 
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
        self.ids.stidcheck.text=""     
        
class Bookupdate(BoxLayout):
    def bcheck(self,instance):
        try:
            t=self.ids.bookcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            self.ids.name.text=row[0]
            self.ids.bid.text=str(row[1])
            self.ids.aname.text=row[2]
            self.ids.e.text=str(row[3])
            self.ids.lan.text=row[4]
            self.ids.py.text=str(row[5])
            self.ids.pname.text=row[6]
            self.ids.bno.text=str(row[7])
            self.ids.nbt.text=str(row[8])
            self.ids.bna.text=str(row[9])
            self.ids.an.text=str(row[10])
            self.ids.bpri.text=str(row[11])
            self.ids.bcn.text=str(row[12])
            self.ids.sr.text=row[13]
        except Exception as e :
            popup = Popup(title="Message",
                      content=Label(text="Book not found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            print(e)
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
    def click(self,instance):
        try:
            t=self.ids.bookcheck.text
            c1=self.ids.name.text
            c2=self.ids.bid.text
            c3=self.ids.aname.text
            c4=self.ids.e.text
            c5=self.ids.lan.text
            c6=self.ids.py.text
            c7=self.ids.pname.text
            c8=self.ids.bno.text
            c9=self.ids.nbt.text
            c10=self.ids.bna.text
            c11=self.ids.an.text
            c12=self.ids.bpri.text
            c13=self.ids.bcn.text
            c14=self.ids.sr.text
            conn.commit()
            if c1!="" and c2!="" and c3!="" and c4!="" and c5!="" and c6!="" and c7!="" and c8!="" and c9!="" and c10!="" and c11!="" and c12!=" and c13!=""" and c14!="":
                cursor.execute('''UPDATE Book SET Bookname =?,
                               Book_Id =?,
                               Author_name =?,
                               Edition =?,
                               Language=?,
                               Pubilication_year=?,
                               Pubilcation_name =?,
                               Book_no=?,
                               No_of_taken=?,
                               No_of_book_aviable =?,
                               Accession_no=?,
                               Book_price=?,
                               classification_no =?,
                               Source=?
                               WHERE Book_Id=?''', (c1,int(c2),c3,int(c4),c5,int(c6),c7,int(c8),int(c8),int(c10),int(c11),float(c12),int(c13),c14,t))
                conn.commit()
                popup = Popup(title="Message",
                      content=Label(text="Updated Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
                popup.open()
                self.ids.header.opacity=0
                self.ids.container.opacity=0
                self.ids.header.disabled=True
                self.ids.container.disabled=True
                self.ids.bookcheck.text=""
            else:
                popup = Popup(title="Message",
                      content=Label(text="Fill the all form",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(500, 400))
                popup.open()       
        except Exception as e:
            popup = Popup(title="Message",
                      content=Label(text="Fill the all form",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(500, 400))
            popup.open()       
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.bookcheck.text
        self.ids.container.disabled=True
class Studentupdate(BoxLayout):
   def check(self,instance):
        try:
            t=self.ids.stidcheck.text
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE student_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            self.ids.name.text=row[0]
            self.ids.stid.text=str(row[1])
            self.ids.program.text=row[2]
            self.ids.faculity.text=row[3]
            self.ids.batch.text=str(row[4])
            self.ids.level.text=row[5]
            self.ids.mbno.text=str(row[6])
            self.ids.email.text=row[7]
            self.ids.dob.text=row[8]
            self.ids.sex.text=row[9]
            self.ids.status.text=row[10]
            self.ids.mnbt.text=str(row[11])
            self.ids.nbt.text=str(row[12])
            self.ids.fname.text=row[13]
        except Exception as e:
            popup = Popup(title="Message",
                      content=Label(text="Student not found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            print(e)
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
   def click(self,instance):
        try:
            t=self.ids.stidcheck.text
            c1=self.ids.name.text
            c2=self.ids.stid.text
            c3=self.ids.program.text
            c4=self.ids.faculity.text
            c5=self.ids.batch.text
            c6=self.ids.level.text
            c7=self.ids.mbno.text
            c8=self.ids.email.text
            c9=self.ids.dob.text
            c10=self.ids.sex.text
            c11=self.ids.status.text
            c12=self.ids.mnbt.text
            c13=self.ids.nbt.text
            c14=self.ids.fname.text
            
            if c1!="" and c2!="" and c3!="" and c4!="" and c5!="" and  c6!="" and c7!="" and  c8!="" and  c9!="" and  c10!="" and  c11!="" and  c12!="" and  c13!="":
                cursor.execute('''UPDATE Student SET Studentname =?,
                               student_Id=?,
                               Program =?,
                               Faculity =?,
                               Batch =?,
                               Level =?,
                               Mobile_no =?,
                               Email =?,
                               Date_brith=?,
                               Gender=?,
                               Status=?,
                               Maxbooktake=?,
                               Noofbooktake=?,
                               Father_name=?
                               WHERE student_Id=?''',(c1,int(c2),c3,c4,int(c5),c6,int(c7),c8,c9,c10,c11,int(c12),int(c13),c14,t))
                conn.commit()
                popup = Popup(title="Message",
                      content=Label(text="Updated Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
                popup.open()
                self.ids.stidcheck.text=""
                self.ids.header.opacity=0
                self.ids.container.opacity=0
                self.ids.header.disabled=True
                self.ids.container.disabled=True
                self.ids.stidcheck.text=""
            else:
                popup = Popup(title="Message",
                      content=Label(text="Fill in the all details ",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(400, 400))
                popup.open()       
        except Exception as e:
            print(e)    
   def back(self,instance):
        self.ids.stidcheck.text=""
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
            
class Bookupdelete(BoxLayout):
    def bcheck(self,instance):
        try:
            t=self.ids.bookcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            self.ids.name.text=row[0]
            self.ids.bid.text=str(row[1])
            self.ids.aname.text=row[2]
            self.ids.e.text=str(row[3])
            self.ids.lan.text=row[4]
            self.ids.py.text=str(row[5])
            self.ids.pname.text=row[6]
            self.ids.bno.text=str(row[7])
            self.ids.nbt.text=str(row[8])
            self.ids.bna.text=str(row[9])
            self.ids.an.text=str(row[10])
            self.ids.bpri.text=str(row[11])
            self.ids.bcn.text=str(row[12])
            self.ids.sr.text=row[13]
        except:
            popup = Popup(title="Message",
                      content=Label(text="Book not found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
    def click(self,instance):
        try:
            t=self.ids.bookcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            if row[7]==row[9]:
                cursor.execute("DELETE FROM Book WHERE Book_Id ="+t)
                conn.commit()
                popup = Popup(title="Message",
                      content=Label(text="Deleted Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
                popup.open()
                self.ids.header.opacity=0
                self.ids.container.opacity=0
                self.ids.header.disabled=True
                self.ids.container.disabled=True
                self.ids.bookcheck.text=""
            else:
                popup = Popup(title="Message",
                      content=Label(text="Book had taked boook by Student so cannot deleted",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(500, 400))
                popup.open()  
                self.ids.bookcheck.text=''     
        except Exception as e:
            print(e)
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
        self.ids.bookcheck.text=""
            
class Studentdelete(BoxLayout):
    def check(self,instance):
        try:
            t=self.ids.stidcheck.text
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE student_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            self.ids.name.text=row[0]
            self.ids.stid.text=str(row[1])
            self.ids.program.text=row[2]
            self.ids.faculity.text=row[3]
            self.ids.batch.text=str(row[4])
            self.ids.level.text=row[5]
            self.ids.mbno.text=str(row[6])
            self.ids.email.text=row[7]
            self.ids.dob.text=row[8]
            self.ids.sex.text=row[9]
            self.ids.status.text=row[10]
            self.ids.mnbt.text=str(row[11])
            self.ids.nbt.text=str(row[12])
            self.ids.fname.text=row[13]

        except Exception as e:
            popup = Popup(title="Message",
                      content=Label(text="Student not found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            print(e)
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
    def click(self,instance):
        try:
            t=self.ids.stidcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE student_Id="+t)
            row = cursor.fetchone()
            conn.commit()
            if row[12]==0:
                cursor.execute("DELETE FROM Student WHERE student_Id ="+t)
                conn.commit()
                popup = Popup(title="Message",
                      content=Label(text="Deleted Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
                popup.open()
                self.ids.header.opacity=0
                self.ids.container.opacity=0
                self.ids.header.disabled=True
                self.ids.container.disabled=True
                self.ids.stidcheck.text=""
            else:
                popup = Popup(title="Message",
                      content=Label(text="Student have taked boook so cannot deleted",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(400, 400))
                popup.open()       
        except Exception as e:
            print(e)
        
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
            
class Tabpl(TabbedPanel):
        pass
class Rott(ScreenManager):
    pass
class Home(Screen):
    def sread(self,instance):
        print("heloo")
        
class Studentadd(Screen):
    def submit(self,instance,rt):
        try:
            cursor = conn.cursor()
            name=rt.ids.sname.text.upper()
            sid=int(rt.ids.sid.text)
            program=rt.ids.sprogram.text
            faculity=rt.ids.sfact.text
            batch=int(rt.ids.sbatch.text)
            level=rt.ids.slevel.text
            mobileno=int(rt.ids.smobileno.text)
            email=rt.ids.semail.text
            dateob=rt.ids.sdate.text
            genger=rt.ids.ssex.text
            status=rt.ids.status.text
            maxbt=int(rt.ids.mb.text)
            nobt=int(rt.ids.nb.text)
            fn=rt.ids.fname.text
            if name!=''and rt.ids.sid.text!='' and program!="" and faculity!="" and rt.ids.sbatch.text!="" and level!="" and rt.ids.smobileno.text!="" and email!="" and dateob!="" and genger!="" and status!="" and rt.ids.mb.text!="" and rt.ids.nb.text!="":
                cursor.execute("INSERT INTO Student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (name,sid,program,faculity,batch,level,mobileno,email,dateob,genger,status,maxbt,nobt,fn))
                popup = Popup(title="Message",
                                content=Label(text='''Added Successfully'''),
                                size_hint=(None, None),
                                size=(300, 200))
                conn.commit()
                popup.open()
            else:
                popup = Popup(title="Message",
                                content=Label(text='''Fill the all details'''),
                                size_hint=(None, None),
                                size=(300, 200))
                popup.open()
                
        except Exception as e:
            t='''Fill the all forms or
            Your entered data is worng'''
            popup = Popup(title="Message",
                      content=Label(text=t,pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
class Bookadd(Screen):
    def submit(self,instance,rt):
        try:
            cursor = conn.cursor()
            name=rt.ids.bname.text.upper()
            sid=int(rt.ids.bid.text)
            program=rt.ids.bauthor.text
            faculity=int(rt.ids.be.text)
            batch=rt.ids.bl.text
            level=int(rt.ids.bpy.text)
            mobileno=rt.ids.bpn.text
            email=int(rt.ids.bn.text)
            dateob=int(rt.ids.bnt.text)
            genger=int(rt.ids.ba.text)
            ac=int(rt.ids.an.text)
            bpr=int(rt.ids.bpri.text)
            cln=int(rt.ids.bcn.text)
            src=rt.ids.sr.text
            cursor.execute("INSERT INTO Book VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (name,sid,program,faculity,batch,level,mobileno,email,dateob,genger,ac,bpr,cln,src))
            conn.commit()
            popup = Popup(title="Message",
                      content=Label(text='''Added Successfully'''),
                      size_hint=(None, None),
                      size=(400, 400))
            popup.open() 
        except Exception as e:
            t='''Student may added or
            Your entered data is'''
            popup = Popup(title="Message",
                      content=Label(text=t),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
class Listadd(Screen):
    def submit(self,instance,rt):
        try:
            cursor = conn.cursor()
            name=rt.ids.blname.text
            sid=int(rt.ids.blid.text)
            program=rt.ids.slname.text
            faculity=int(rt.ids.slid.text)
            batch=rt.ids.isdate.text
            mobileno="s"+rt.ids.blid.text+rt.ids.slid.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id ="+rt.ids.blid.text)
            bookd = cursor.fetchone()
            conn.commit()
            cursor.execute("SELECT * FROM Student WHERE student_Id="+rt.ids.slid.text)
            st= cursor.fetchone()
            conn.commit()
            if bookd[9]>0 and st[11]>st[12] and st[10]=="Eligible":
                cursor = conn.cursor()    
                cursor.execute("INSERT INTO LBT VALUES (?,?,?,?,?,?)",(name,sid,program,faculity,batch,mobileno))
                av=bookd[9]-1
                print()
                ay=st[12]+1
                cursor.execute('''UPDATE Book SET No_of_book_aviable=? WHERE Book_Id=?''',(av,rt.ids.blid.text))
                cursor.execute('''UPDATE Student SET Noofbooktake=? WHERE student_Id=?''',(ay,rt.ids.slid.text))
                conn.commit()
                popup = Popup(title="Message",content=Label(text='''Added Successfully'''),
                            size_hint=(None, None),
                                size=(400, 400))
                popup.open()
                
            else:
                popup = Popup(title="Message",
                            content=Label(text='''He is not able to take book'''),
                            size_hint=(None, None),
                            size=(400, 400))
                popup.open()
                            
        except Exception as e:
            t='''List may added or
            Your entered data is'''
            popup=Popup(title="Message",content=Label(text=t),size_hint=(None, None),size=(300, 200))
            popup.open() 
            print(e)
class Login(Screen):
    def login(self,instance,rot):
        p=rot.ids.pswrd.text
        y=rot.ids.user.text
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User ")
        row = cursor.fetchone()
        if y==row[0] and p==row[1]:
            self.manager.current="home"
            rot.ids.pswrd.text=""
            rot.ids.user.text=""
            
        elif y=="" and p=="":
            rot.ids.inter.disabled=False
            rot.ids.inter.opacity=1
            rot.ids.inter.text="Please enter details"    
        else:
            rot.ids.pswrd.text=""
            rot.ids.user.text=""
            rot.ids.inter.disabled=False
            rot.ids.inter.opacity=1
            rot.ids.inter.text="Worng details" 
            
class Loginbox(BoxLayout):
    def login1(self,instance):
        a=Login() 
        a.login(a) 
class User(BoxLayout):
    def login1(self,instance):
        a=Login() 
        a.login(a)     
class UserPassword(Screen):
    def login(self,instance,rot):
        try:
            p=rot.ids.pswrd.text
            u=rot.ids.user.text
            y=rot.ids.pswrd2.text
            if y==p:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM User ")
                row = cursor.fetchone()
                cursor = conn.cursor()
                cursor.execute('''UPDATE User SET  User =?,
                                Password=?
                                WHERE User=? and Password=?''',(u,y,row[0],row[1]))
                conn.commit()
                popup = Popup(title="Message",
                        content=Label(text="Sucessfull Updated\n"+"user ="+u+"\n password= "+y,pos_hint={'center_x':0.5,'center_y':0.5}),
                            size_hint=(None, None),
                        size=(300, 200))
                popup.open()
                rot.ids.pswrd.text=""
                rot.ids.pswrd2.text=""
                rot.ids.user.text=""
            elif y=="" and p=="":
                rot.ids.inter.disabled=False
                rot.ids.inter.opacity=1
                rot.ids.inter.text="Please enter details"    
            else:
                rot.ids.pswrd.text=""
                rot.ids.pswrd2.text=""
                rot.ids.user.text=""
                rot.ids.inter.disabled=False
                rot.ids.inter.opacity=1
                rot.ids.inter.text="NOT MATCH YOUR PASSWORD" 
        except Exception as e:
            print(e)
    def back(self,instance,rot):
        rot.ids.pswrd.text=""
        rot.ids.pswrd2.text=""
        rot.ids.user.text=""
            
class Studentdetials(BoxLayout):
    pass
class Bookdetials(BoxLayout):
    pass
class Listupdate(BoxLayout):
    def bcheck(self,instance):
        try:
            t=self.ids.bookcheck.text
            t1=self.ids.studentcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM LBT WHERE Book_id="+t+" and student_Id="+t1)
            row1 = cursor.fetchone()
            conn.commit()
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            self.ids.bname.text= row1[0]
            self.ids.bid.text=str(row1[1])
            self.ids.sname.text=row1[2]
            self.ids.sid.text=str(row1[3])
            self.ids.isdate.text=row1[4]
        except Exception as e:
            popup = Popup(title="Message",
                      content=Label(text="Not Found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            print(e)
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
        self.ids.bookcheck.text=""
        self.ids.studentcheck.text=""
    def click(self,instance):
        try:
            t=self.ids.bookcheck.text
            t1=self.ids.studentcheck.text
            c1=self.ids.bname.text
            c2=self.ids.bid.text
            c3=self.ids.sname.text
            c4=self.ids.sid.text
            c5=self.ids.isdate.text
            if c1!="" and c2!="" and c3!="" and c4!="" and c5!="":
                cursor.execute('''UPDATE LBT SET  Bookname =?,
                               Book_id=?,
                               Student_name=?,
                               student_Id =?,
                               Issue_date =?
                                WHERE student_Id=? and Book_id=?''',(c1,int(c2),c3,int(c4),c5,t1,t))
                conn.commit()
                popup = Popup(title="Message",
                      content=Label(text="Updated Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
                popup.open()
                self.ids.header.opacity=0
                self.ids.container.opacity=0
                self.ids.header.disabled=True
                self.ids.container.disabled=True
                self.ids.bookcheck.text=""
                self.ids.studentcheck.text=""
            else:
                popup = Popup(title="Message",
                      content=Label(text="Fill in the all details ",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(400, 400))
                popup.open()       
        except Exception as e:
            print(e)    
    
class Listdelete(BoxLayout):
    def bcheck(self,instance):
       try:
            t=self.ids.bookcheck.text
            t1=self.ids.studentcheck.text
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM LBT WHERE Book_id="+t+ " and student_Id="+t1)
            row1 = cursor.fetchone()
            conn.commit()
            self.ids.header.opacity=1
            self.ids.container.opacity=1
            self.ids.header.disabled=False
            self.ids.container.disabled=False
            self.ids.bname.text= row1[0]
            self.ids.bid.text=str(row1[1])
            self.ids.sname.text=row1[2]
            self.ids.sid.text=str(row1[3])
            self.ids.isdate.text=row1[4]
       except Exception as e:
            popup = Popup(title="Message",
                      content=Label(text="Not Found",pos_hint={'center_x':0.5,'center_y':0.5}),
                      size_hint=(None, None),
                      size=(300, 200))
            popup.open()
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True
    def back(self,instance):
        self.ids.header.opacity=0
        self.ids.container.opacity=0
        self.ids.header.disabled=True
        self.ids.container.disabled=True
        self.ids.bookcheck.text=""
        self.ids.studentcheck.text=""
    def click(self,instance):
        try:
            t=self.ids.bookcheck.text
            t1=self.ids.studentcheck.text
            cursor = conn.cursor()
            cursor.execute("DELETE FROM LBT WHERE  Book_id = "+t+" and student_Id="+t1)
            conn.commit()
            popup = Popup(title="Message",
                    content=Label(text="Deleted Sucessfully",pos_hint={'center_x':0.5,'center_y':0.5}),
                    size_hint=(None, None),
                    size=(300, 200))
            popup.open()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Book WHERE Book_Id ="+self.ids.bookcheck.text)
            bookd = cursor.fetchone()
            conn.commit()
            cursor.execute("SELECT * FROM Student WHERE student_Id= "+self.ids.studentcheck.text)
            st= cursor.fetchone()
            conn.commit()
            av=bookd[9]+1
            ay=st[12]-1
            cursor = conn.cursor()
            cursor.execute('''UPDATE Book SET No_of_book_aviable=? WHERE Book_Id=?''',(av,t))
            cursor.execute('''UPDATE Student SET Noofbooktake=? WHERE student_Id=?''',(ay,t1))
            conn.commit()
            self.ids.header.opacity=0
            self.ids.container.opacity=0
            self.ids.header.disabled=True
            self.ids.container.disabled=True  
            self.ids.bookcheck.text=""
            self.ids.studentcheck.text=""
        except Exception as e:
            print(e)    

class MyApp(App):
    icon="iconlib.png"
    title="LIBRARY MANGEMENT SYSTEM"
    name="LIBRARY MANGEMENT SYSTEM"
    def build(self):
        return Rott()
MyApp().run()
conn.close()
