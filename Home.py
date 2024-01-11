# This is a sample Python script.
import pandas
import streamlit as st

st.set_page_config(layout="wide")

st.title("Anurag Patwardhan")

col1, col2 = st.columns(2)

content = """Hello, welcome to my website. I am a software engineer and 
full-time coder with 10+ years of experience in both Development and Support projects. 
I have worked in the Insurance, Banking, Law and publication domain with clients across the European Union, 
North America and Australia and have been recognized with several awards during my career.Currently, 
I am working as Consultant at Luxoft and providing my best level in the role and responsibilities assigned to me. """

content2 = """I am always eager to learn new technology and skills and upgrade my skill as per need of client.
I have good hand on experience working as Functional analyst as well as technical analyst. 
Previous experience includes working with CMM Level 5 company namely Accentuer and Infosys.
I have good hand-on experience of working in different technology."""

content3 = """Technology : Mainframe (PL/1, Cobol, JCL, DB2,MQ,CICS), Python, Perl, Java (studs), VB.net, HTML
Functional Domain : Insurance ( Underwriting & Claims), Banking (loan and Cards & Payment) , Law and Publications"""

content4 = """My colleagues know me as highly creative with good analytical skills and can always be trusted with resolving technical issues. I have a good understanding of various domain functionality and am always eager to learn new skills. 
I know that the client’s business comes first, and client satisfaction is always a priority. I spend a suitable amount of time understanding the business and the audience before suggesting the implementation and development of solution code. I have good experience in leading the team in multiple projects. 
I have worked under Agile, DevOps and SDLC (V model) methodology 
I have done my post-graduation degree M.C.A. from the International Institute of Professional Studies, DAVV university."""

content5 = """ Below are various organization i have worked and learned various skill of software engineering """
content6 = """ I have made this website as part of learning process to learn Python and various streamlit utilities"""



with col1:
    st.image("images/photo.jpg" , width=400)

with col2:
    #st.write(content)
    st.info(content)
    st.info(content2)
    st.info(content3)

st.info(content4)

st.write(content6)

st.write(content5)

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=",")
df1 = pandas.read_csv("data1.csv",sep=",")

with col3:
    for index, row in df.iterrows():
        st.subheader(row["title"])
        #st.write(row["Country"])
        st.image("images/" + row["image"])

with col4:
    for index, row in df1.iterrows():
        st.subheader(row["title"])
        st.write(row["Country"])
        st.image("images/" + row["image"])




#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
