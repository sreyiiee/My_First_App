import streamlit as st
import pandas as pd

#page settings
st.set_page_config(
    page_title="Smart AI Lab - Introduction to Machine Learing",
    layout="wide"
)

#sidebar
st.sidebar.title("Smart AI Lab")
st.sidebar.write(
    "Explore the basics of Machine Learning and see "
    "how Streamlit can be used to build interactive ML applications."
)

page=st.sidebar.radio(
    "Choose a topic",
    [
        "Start Here",
        "AI and Machine Learning",
        "How Mahcines Learn",
        "Types of Machine Learing",
        "Choose the Right Approach",
        "ML in Different Industries",
        "ML Project Lifecycle",
        "Final Challenge"
    ]
)

#Start here
if page=="Start Here":
    st.title("Smart AI Lab")
    st.write("""Welcome to the first session of our Machine Learning Journey.
    Imagine that you have joined the analytics team of a bank.
    The business team does not start by telling you which
    Machine Learing Algorithm to use.
    They start wuth a business problem.
    """)
    st.divider()
    st.subheader("The bank has three questions")
    col1, col2, col3=st.columns(3)
    with col1:
        st.markdown("#### Prediction")
        st.write("""
        Can we predict whether a customer is likely
        to default on a loan?
        """)
    with col2:
        st.markdown("#### Discovery")
        st.write("""
        Can we discover different types of cutsomers
        from data?
        """)
    with col3:
        st.markdown("#### Decision")
        st.write("""
        Can a machine learn which action is better

        """)
    st.divider()

    st.write("""
      these three questions are all related to Machine Learning,
      but they represent different learning problems.

      during this session we will understand the difference
      between them and also see how Streamlit can help us
      turn our ideas into interactive application.
      """)
    st.info("the goal of this session is understanding,not model building.")

#AI and Machine Learning
elif page == "AI and Machine Learning":
     st.title("Artifical Inteligence and Machine Learning")

     st.write("""
     Before learning Machine Learning, we need to understand where it fits into the larger field of 
     artifical intelligence
     """)

     st.subheader("Artifical intelligence")
     st.write("""
     artifical Inteligence is the border field of creating computer systems that can perform tasks taht normally
     require human intelligence.
     these tasks can include learning,reasoning,langugae undersanding, planning and decision-making.
     """)
     st.subheader("Machine Learning")
     st.write("""
     Machine Learning is a subset of Artificial Intelligence.
     Instead of explicitly programming every rule, we provide
     data to a Machine Learning System and allow it to learn
     patterns from that data.
     Those learned patterns can then be used to make predictions,
     identify patterns or support decisions.
     """)

     st.subheader("Deep Learning")
     st.write("""
     Depp Learning is a subset of Machine Learning based on
     multi-layer neural networks.
     It is particularly useful when working with comples data
     such as images, speech, video and large amounts of text.
     """)
     st.divider()

     st.markdown("""
     **Artificial Intelligence** - A broad field concerned with intelligent behaviour.
     **Machine Learning** - A way of building AI systems that learn patterns from data.
     **Deep Learning** - A family of Machine Learning based on multi-layer neural networks.
     """)
     st.divider()
     st.subheader("Smart Banking")

     st.write("""
     consider a banking application.
     AI could refer to the overall intelligent system.
     Machine Laerning could be used for:
    -predicting loan default
    -detecting unusal transition
    -forecasting demand
    -understanding customer behaviour

    Deep Laerning could be useful for:
    -analysing documents
    -speech recognition
    -understanding text
    - image based document processing
    """)

#How machine Learn
elif page=="How Machines Learn":
    st.title("What Does It Mean For a Machine to Learn")
    st.write("""
    In traditional programming, we normally provide rules and 
    data to produce an output.
    """)
    st.subheader("Traditional programming")
    st.markdown("""
    **Rules + Data = Output**
    """)
    st.write("""
    Example: A programmer may explicitely write rules such as:
    If transaction amount is greater than a particular value
    and the transaction happens in an unusual location,
    flag the transaction.
    This works well when the rules are known can be 
    clearly written.
    """)

    st.divider()
    st.subheader("Machine Learning")
    st.markdown("""
    **Data + Expected outcomes -> Learning process -> Model**
    """)
    st.write("""
    In Machine Learning, instead of manually writing evry tule,
    we provide examples to a learning system.
    The system tries to identify patterns in those examples.
    The result is a model that can be used on new data.
    """)
    st.divider()
    st.subheader("Smart Banking")
    st.write("""
    Suppose a bank has historical customer information.
    For each customer we may have:
    - income
    - age
    - credit history
    - loan amount
    - repayment behaviour

    If we also know whether those customers eventually
    defaulted, we can use those historical examples to
    learn a relationship between the customer information
    and the outcome.    
    """)
    st.write("""
    The important idea is:
    **The model learns from examples rather than being given
    every rule explicitly.**
    """)
    st.divider()

