# Add images for social, political, legal and ethical sections

import streamlit as st

st.set_page_config("Olbtech Electronics", page_icon="logo.png", layout="wide")

sect = st.sidebar.radio("**:red[Navigation:]**", ["Homepage", "Product Lines", "STEEPLE Analysis: Nigeria", "Sources"])

st.write("---")
st.markdown(f'<h1 style="color:yellow;">{sect}</h1>', unsafe_allow_html=True)
st.write("---")

if sect == "Homepage":
    st.write("We are a leading Canadian electronics and hardware company that designs, manufactures, and services advanced electronic devices.")
    st.write("Currently, we are looking at expanding our operations by establishing a new factory in **Nigeria**.")
    st.write("This expansion is intended to:")
    st.write("""
- **Lower** production costs
- **Improve** manufacturing quality
- **Speed up** product delivery
- **Access emerging** markets    
    """)

if sect == "Product Lines":
    st.subheader("**Our Product Lines Are:**")
    st.write("""
    - **Consumer Electronics**: Smartphones, tablets, and smart home devices.
    - **Medical Devices**: Portable diagnostic equipment and wearable health monitors.
    - **Industrial Equipment**: Automated machinery controllers and sensors.
    - **Renewable Energy Solutions**: Solar panels and energy storage systems.
    - **Automotive Components**: Infotainment systems and electric vehicle (EV) battery management systems.
    """)

if sect == "STEEPLE Analysis: Nigeria":

    steeples = [":red[**S***ocial*]", ":blue[**T***echnological*]", ":orange[**E***conomical*]", ":green[**E***nvironmental*]", ":violet[**P***olitical*]", ":grey[**L***egal*]", ":rainbow[**E***thical*]"]
    ex1, ex2, ex3, ex4, ex5, ex6, ex7 = [st.expander(f"{i}") for i in steeples]
    steeplesexp = [ex1, ex2, ex3, ex4, ex5, ex6, ex7]
    steeples = [":red[Social]", ":blue[Technological]", ":orange[Economical]", ":green[Environmental]", ":violet[Political]", ":grey[Legal]", ":rainbow[Ethical]"]

    for steeple, exp in zip(steeples, steeplesexp):
        exp.header(steeple)

    social = """

    2022:
    --

      - Bandits (groups of nomadic herdsmen that have conflicts with farming communities) carried out kidnappings for ransom, mass killings and rape,
        and raided communities across the region.
      - Over 100 bandit groups (avg. 30 members each) operate with military grade weapons in mostly ungoverned areas.
    ---
    """

    technological = """
    2023:
    --

    - Inadequate infrastructure, limited access to affordable internet and an unstable power supply network all pose a threat to possible technological developments.
    - High risks of cyber-crime, data breaches and identity theft, which can easily compromise corporate networks.
    - Data collection, use and storage methods raise many privacy concerns, introducing the need for complex data protection regulations and awareness.
    - A clear digital divide (between urban and rural areas) and socioeconomic inequality leads to very unequal distribution in access to technology, furthering
      the already existing inequalities that exist.
    - In urban areas, 67% of men and 46% of women used mobile internet, but in rural areas, only 41% of men and 24% of women had access to mobile internet (GSMA 2021 Customer Survey).
    ---
    """
    
    economical = """
    2021:
    --

      - GDP per Capita: $2065.75
      - Gini Index: 35.1
      - The federal government officially announced that 2 million househlds are benefiting from its Conditional Cash Transfer (CCT) program.
      - Food inflation reached 22% in July, leading to families struggling to afford food.
      - Over 95 million Nigerians are living in poverty (estimated 1.90 USD per day, World Bank); Human Rights Watch Research
        found that Nigeria does not have a working social protection system to protect citizens from economic shocks.
    ---
    """
    
    environmental = """
    2021
    --

    - Main Issues: high air & water pollution, oil spillage, deforestation, desertification, erosion and flooding (due to insufficient drainage systems),
      mostly (directly or indirectly) caused by human activity.
    - Evaluation on the Global Burden of Disease (GBD) confirmed the causes of death and Disability-Adjusted Life Years (DALYs) in Nigeria from 2007-2017.
    - The lower respiratory infection caused by air pollution had gone from the 4th (2007) to the highest-ranked (2017) cause of death.
    - Other causes of death (related to environmental factors) included chronic respiratory diseases, cardiovascular diseases, enteric infections, diarrheal-, contagion-, maternally- and nutritionally-related diseases.
    ---
    """
    
    political = """
    2022:
    --

      - 40 worshippers at a church in Southwest Ondo State were killed by gunfire.
      - Various attacks by Islamist and other armed groups near Nigeria's seat of government in Abuja.
      - The United States government approved the sale of 12 AH-1Z attack helicopters and related military
        equipment for $997 million to the Nigerian government; this sale had been suspended in 2021 due to
        human rights' concerns.
      - An Intercept report in July reported possible US involvement in Nigerian military air strikes that had
        taken place in 2017, which the Nigerian authorities had stated were intnded to hit Boko Haram (terrorist group)
        targets, but instead had killed over 160 displaced people - mostly children - in a camp located in Rann, Borno
        State.
      - Members of Boko Haram - a prevalent terrorist group in Nigeria - have been involved in various crimes in the Southwest, including an attack on a prison in Kuje that was 40km
        from the capital city, Abuja; this attack freed 900 inmates, 60 of which were Boko Haram, with Ansaru - a recent Al-Quaeda-backed splinter (related, but independent) faction of
        Boku Haram.
    ---
    """
    
    legal = """
    2022:
    --

      - 81% of all Nigerians experienced 1 or more legal problems.
      - Most common legal problems were disputes with neighbors, domestic violence, land disputes, general crime and housing problems.
      - Most people with legal problems experience losses of time, money, or other negative consequences.
      - Nigerians tend to seek legal help mostly within their social circle, but also sometimes turn to the police, traditional leaders/communities,
        religious authorities, landlords, lawyers or local public authorities when they need additional help.
    ---
    """
    
    ethical = """
    2021:
    --
      - Human Rights Watch Research found that required initiatives like the CCT program could not protect people's rights to a decent
        standard of living during the SARS-CoV-19 (CoViD-19) pandemic.
      - Expressing views against **Sharia** (Islamic Law) is criminalized, despite it's sexism against the female population, binding them to their husbands and
        treating them as items or tools; not individuals.
      - In March, lawmakers had rejected proposed amendments - made to fostor women's rights and political participation - to the Nigerian Constitution, including
        granting citizenship to foreign husbands of Nigerian women (which was already done for foreign wives of Negierian men) as well as to include more
        affirmative actions to make sure there are more women participating in leadership.
    ---
    """

    ex1.write(social)
    ex1.image("https://cdn.britannica.com/93/168093-050-529284A0/Nigeria-Areas-Boko-Haram.jpg?w=400&h=300&c=crop", caption="Boko Haram Activity in Nigeria: https://www.britannica.com/topic/Boko-Haram")

    ex2.write(technological)
    ex2.image("https://diinsiderlife.com/wp-content/uploads/2023/08/2-1.png", caption="https://diinsiderlife.com/index.php/2023/08/10/exposing-the-gender-divide-in-nigerian-digital-literacy/")

    ex3.write(economical)
    ex3.image("https://i0.wp.com/www.dataphyte.com/wp-content/uploads/2022/07/Nigerias-Public-Debt-cover-image.png?fit=1200%2C675&ssl=1", caption="https://i0.wp.com/www.dataphyte.com/wp-content/uploads/2022/07/Nigerias-Public-Debt-cover-image.png?fit=1200%2C675&ssl=1")

    ex4.write(environmental)
    ex4.image("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8022161/bin/gr2.jpg", caption="Distribution of Environmental Problems Across Nigeria: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8022161/")

    ex5.write(political)
    ex5.image("https://acleddata.com/acleddatanew/wp-content/uploads/2023/02/image3-1.png", caption="https://acleddata.com/2023/02/22/political-violence-and-the-2023-nigerian-election/")
    
    ex6.write(legal)
    ex6.image("https://www.researchgate.net/profile/Adenuga-Adekoya/publication/348656287/figure/fig1/AS:982395759116288@1611232809165/Violent-crime-in-Nigeria-from-2013-to-2017-Source-Author-Compilation-based-on-Nigeria.png", caption="https://www.researchgate.net/figure/Violent-crime-in-Nigeria-from-2013-to-2017-Source-Author-Compilation-based-on-Nigeria_fig1_348656287")
    
    ex7.write(ethical)
    ex7.image("https://fundforpeace.org/wp-content/uploads/2018/08/20150325-1.png", caption="https://fundforpeace.org/2015/03/25/gender-violence-spikes-in-nigerian-election-run-up/")

if sect == "Sources":
    src = """
    - “World Report 2023: Rights Trends in Nigeria.” World Report 2023 | Human Rights Watch, Human Rights Watch, 20 Jan. 2023, www.hrw.org/world-report/2023/country-chapters/nigeria. 
    - “Nigeria.” Nigeria - Place Explorer - Data Commons, Data Commons, www.datacommons.org/place/country/NGA?utm_medium=explore&mprop=count&popt=Person&hl=en. Accessed 19 May 2024.
    - “Justice Needs and Satisfaction in Nigeria.” HiiL, The Hague Institute for Innovation of Law, 9 May 2023, www.hiil.org/research/justice-needs-and-satisfaction-in-nigeria/#:~:text=The%20most%20common%20legal%20problem,address%20their%20most%20serious%20problem. 
    - Pona, Hyellai Titus, et al. “Environmental Health Situation in Nigeria: Current Status and Future Needs.” Environmental Health Situation in Nigeria: Current Status and Future Needs - PMC, U.S. National Library of Medicine, 23 Mar. 2021, www.ncbi.nlm.nih.gov/pmc/articles/PMC8022161/.
    - Iheduba, Kelechi. “Exploring the Impact of Technology on Nigerian Society: Opportunities, Challenges, and Ethical Considerations.” LinkedIn, LinkedIn, 14 July 2023, www.linkedin.com/pulse/exploring-impact-technology-nigerian-society-ethical-kelechi-iheduba-.
    - “Helping to Bridge the Digital Divide in Nigeria.” Tech Herfrica, 29 Apr. 2024, www.techherfrica.org/tech-herfrica-helping-to-bridge-the-digital-divide-in-nigeria/#:~:text=According%20to%20a%20report%20from,economic%20growth%2C%20and%20social%20connection.
    """
    st.write(src)
