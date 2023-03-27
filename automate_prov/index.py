import streamlit as st

# Set page title
st.set_page_config(page_title="N2P Auto Provisioning")

# Add page title
st.title("N2P Auto Provisioning")

# Add text input and button to confirm search
search_query = st.text_input("Enter search query:")
search_button = st.button("Search")

# Add file input
uploaded_file = st.file_uploader("Upload file")

# Add a divider
st.markdown("---")

# Add information section with placeholders
st.subheader("Information")
ramal = st.empty()
serial = st.empty()
mac = st.empty()
ztp = st.empty()
photo = st.empty()

# Update placeholders with dummy data when search button is clicked
if search_button:
    ramal.text("Ramal: 1234")
    serial.text("Serial: ABCD")
    mac.text("MAC: 00:11:22:33:44:55")
    ztp.text("ZTP: Enabled")
    photo.image("https://via.placeholder.com/150")
