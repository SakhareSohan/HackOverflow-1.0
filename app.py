import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# --- SETTING PAGE CONFIG ---
st.set_page_config(
    page_title="Multiple Disease Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LOADING THE SAVED MODELS ---
# Note: Update the file paths to where you have saved your models.
# It's best practice to keep them in the same directory or a sub-directory.
try:
    diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('./saved_models/heart_disease_model.sav','rb'))
    parkinsons_model = pickle.load(open('./saved_models/parkinsons_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please ensure the 'saved_models' directory and model files are in the correct path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the models: {e}")
    st.stop()


# --- SIDEBAR FOR NAVIGATION ---
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart-pulse','person'],
                          default_index=0)

# --- FUNCTIONS FOR EACH PREDICTION PAGE ---

def diabetes_prediction_page():
    st.title('Diabetes Prediction using ML')
    st.markdown("Enter the patient's details below to predict whether they have diabetes.")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', help="Enter the total number of pregnancies.")
    with col2:
        Glucose = st.text_input('Glucose Level', help="Enter the plasma glucose concentration a 2 hours in an oral glucose tolerance test.")
    with col3:
        BloodPressure = st.text_input('Blood Pressure value (mm Hg)', help="Diastolic blood pressure.")
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (mm)', help="Triceps skin fold thickness.")
    with col2:
        Insulin = st.text_input('Insulin Level (mu U/ml)', help="2-Hour serum insulin.")
    with col3:
        BMI = st.text_input('BMI value', help="Body mass index (weight in kg / (height in m)^2).")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', help="A function that scores likelihood of diabetes based on family history.")
    with col2:
        Age = st.text_input('Age of the Person', help="Enter the age in years.")
    
    if st.button('Predict Diabetes', key='diabetes_predict'):
        try:
            # Convert inputs to float for the model
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure), 
                float(SkinThickness), float(Insulin), float(BMI), 
                float(DiabetesPedigreeFunction), float(Age)
            ]
            
            diab_prediction = diabetes_model.predict([user_input])
            
            if diab_prediction[0] == 1:
                st.error('**Prediction: The person is Diabetic.**')
                st.info("Please advise the patient to consult with a healthcare professional for further evaluation and management.")
            else:
                st.success('**Prediction: The person is Not Diabetic.**')
                st.info("This result indicates a lower likelihood of diabetes, but maintaining a healthy lifestyle is always recommended.")

        except ValueError:
            st.warning("Please enter valid numbers in all fields.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

def heart_disease_prediction_page():
    st.title('Heart Disease Prediction using ML')
    st.markdown("Enter the patient's details below to predict the likelihood of heart disease.")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', help="Age in years.")
    with col2:
        sex = st.text_input('Sex', help="1 = male; 0 = female.")
    with col3:
        cp = st.text_input('Chest Pain types', help="0-3: Type of chest pain.")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Serum Cholestoral (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', help="1 = true; 0 = false.")
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', help="0-2: Values.")
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina', help="1 = yes; 0 = no.")
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', help="0-3: Number of major vessels.")
    with col1:
        thal = st.text_input('Thal rate', help="0 = normal; 1 = fixed defect; 2 = reversible defect.")
        
    if st.button('Predict Heart Disease', key='heart_predict'):
        try:
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), 
                float(fbs), float(restecg), float(thalach), float(exang), 
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            
            heart_prediction = heart_disease_model.predict([user_input])
            
            if heart_prediction[0] == 1:
                st.error('**Prediction: The person has Heart Disease.**')
                st.info("Immediate consultation with a cardiologist is strongly recommended.")
            else:
                st.success('**Prediction: The person does not have Heart Disease.**')
                st.info("Continue to monitor cardiovascular health and maintain a healthy lifestyle.")

        except ValueError:
            st.warning("Please enter valid numbers in all fields.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")


def parkinsons_prediction_page():
    st.title("Parkinson's Disease Prediction using ML")
    st.markdown("This model predicts Parkinson's disease based on vocal measurements.")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    # This is a large number of inputs; consider a more compact layout if needed.
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        PPQ = st.text_input('MDVP:PPQ')
        APQ5 = st.text_input('Shimmer:APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        DDP = st.text_input('Jitter:DDP')
        APQ = st.text_input('MDVP:APQ')
        DFA = st.text_input('DFA')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        Shimmer = st.text_input('MDVP:Shimmer')
        DDA = st.text_input('Shimmer:DDA')
        spread1 = st.text_input('spread1')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')

    if st.button("Predict Parkinson's", key='parkinsons_predict'):
        try:
            user_input = [
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]

            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                st.error("**Prediction: The person has Parkinson's Disease.**")
                st.info("A consultation with a neurologist is advised for further assessment.")
            else:
                st.success("**Prediction: The person does not have Parkinson's Disease.**")
                st.info("This result indicates a lower likelihood of Parkinson's disease based on the vocal metrics provided.")

        except ValueError:
            st.warning("Please enter valid numbers in all fields.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# --- MAIN APP LOGIC ---
if selected == 'Diabetes Prediction':
    diabetes_prediction_page()

if selected == 'Heart Disease Prediction':
    heart_disease_prediction_page()

if selected == "Parkinsons Prediction":
    parkinsons_prediction_page()