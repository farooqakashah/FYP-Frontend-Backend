import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What type of soil is best for cultivating beans in Pakistan?", "Beans perform best in well-drained, sandy loam to clay loam soils rich in organic matter. They are highly sensitive to waterlogged and saline soils.", "Field Preparation"),
    ("How should the field be prepared for sowing beans?", "The field should be deeply ploughed 2-3 times followed by planking to create a fine, loose seedbed, which is crucial for the delicate root system of beans.", "Field Preparation"),
    ("Are beans sown on flat land or ridges?", "It is highly recommended to sow beans on ridges (raised beds) to prevent the roots and stem base from coming into direct contact with irrigation water, which causes rotting.", "Field Preparation"),
    ("What is the optimal row-to-row spacing for bush-type French beans?", "For dwarf/bush varieties, the row-to-row distance is kept at 1.5 to 2 feet (45-60 cm).", "Field Preparation"),
    ("What is the optimal spacing for pole (climbing) beans?", "For climbing beans like Yard Long beans, the row-to-row distance should be wider, around 3 to 4 feet, to allow for staking and trellising.", "Field Preparation"),
    ("What is the optimal plant-to-plant distance for most bean varieties?", "A plant-to-plant distance of 6 to 9 inches is recommended to avoid overcrowding and reduce humidity in the canopy.", "Field Preparation"),
    ("At what depth should bean seeds be sown?", "Seeds should be sown at a depth of 1 to 1.5 inches. Sowing too deep results in poor and delayed germination.", "Field Preparation"),

    # --- Types of Beans & Varieties ---
    ("What are the main types of vegetable beans grown in Pakistan?", "The primary vegetable beans are French Beans (Farash Bean), Yard Long Beans (Rawa/Lobia Phali), and Indian/Dolichos Beans (Sem Phali).", "Varieties"),
    ("What is the difference between bush and pole beans?", "Bush beans are dwarf, self-supporting plants that mature quickly. Pole beans are climbing vines that require staking/trellising and produce over a longer period.", "Varieties"),
    ("What is Dolichos Bean (Indian Bean)?", "Locally known as 'Sem Phali', it is a climbing bean variety characterized by its broad, flat, and often purplish/green pods, widely grown in kitchen gardens and commercial peri-urban farms.", "Varieties"),
    ("What is the Yard Long Bean?", "Known locally as 'Rawa' or 'Bora', it is a climbing vine that produces extremely long, slender, and tender pods, highly popular as a summer vegetable.", "Varieties"),
    ("What are some common varieties of French Bean in Pakistan?", "Common varieties include Contender, Roma (bush type), and Kentucky Wonder (pole type).", "Varieties"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("Why is KPK considered the hub of French bean cultivation?", "The cool, temperate summer climate of northern KPK (Swat, Dir, Kaghan) provides ideal conditions for high-quality French bean production.", "Provincial: KPK"),
    ("When are beans sown in the hilly areas of KPK?", "In the mountainous regions, beans are sown in April-May and harvested continuously throughout the summer.", "Provincial: KPK"),
    ("How does the KPK bean harvest impact national markets?", "The summer crop from KPK supplies fresh French beans to the entire country (including Punjab and Sindh) during the off-season when plains cannot grow them due to extreme heat.", "Provincial: KPK"),

    # --- Provincial: Punjab ---
    ("What are the sowing seasons for beans in the plains of Punjab?", "In the plains, beans are grown in two seasons: Spring (sown in February-March) and Autumn (sown in August-September).", "Provincial: Punjab"),
    ("Why is tunnel farming used for beans in Punjab?", "Walk-in tunnels are used to grow early spring beans, protecting the young plants from January frost and allowing farmers to capture high early-market prices.", "Provincial: Punjab"),
    ("Can beans survive the peak summer heat in Punjab?", "No, high temperatures (above 35°C) in May-July cause severe blossom drop and poor pod set, which is why they are not grown in peak summer in the plains.", "Provincial: Punjab"),
    ("Which type of bean is most popular in Punjab's summer?", "Yard Long beans (Rawa) and Guar (Cluster beans) are more heat-tolerant and are commonly grown during the hot summer months.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("When are beans primarily cultivated in Sindh?", "Due to the warmer climate, French beans in Sindh are mostly grown as an early winter vegetable, sown in October-November.", "Provincial: Sindh"),
    ("Which bean type is very popular in rural Sindh?", "Dolichos bean (Sem Phali) and Cluster bean (Guar) are highly popular and culturally integrated into the local cuisine of Sindh.", "Provincial: Sindh"),
    ("What is the main challenge for bean cultivation in lower Sindh?", "High soil salinity and waterlogging are the main challenges, as beans are highly sensitive to both.", "Provincial: Sindh"),

    # --- Provincial: Balochistan ---
    ("Where are beans grown in Balochistan?", "They are grown as a summer vegetable in the cooler highland valleys like Quetta, Ziarat, and Kalat.", "Provincial: Balochistan"),
    ("When is the crop sown in highland Balochistan?", "Sowing typically occurs in April and May, taking advantage of the mild summer.", "Provincial: Balochistan"),
    ("What restricts larger-scale bean farming in Balochistan?", "The severe scarcity of irrigation water restricts extensive cultivation, as beans require consistent soil moisture.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("Do beans require heavy Nitrogen fertilizer like Urea?", "No, beans are legumes. They have root nodules that fix atmospheric nitrogen, so they require very little external Nitrogen compared to other vegetables.", "Fertilizer Management"),
    ("What is the general NPK dose for French beans?", "A standard basal dose is 1 bag of DAP (for Phosphorus) and half a bag of SOP (Potash) per acre. Urea is applied minimally (half a bag) just to boost initial growth.", "Fertilizer Management"),
    ("Why is Phosphorus (DAP) crucial for beans?", "Phosphorus promotes vigorous root development, which is essential for nodule formation, flowering, and uniform pod setting.", "Fertilizer Management"),
    ("When should micronutrients be applied to beans?", "A foliar spray of micronutrients (Zinc, Boron, and Molybdenum) is highly recommended just before the flowering stage to prevent blossom drop.", "Fertilizer Management"),
    ("What causes yellowing (chlorosis) of bean leaves if pests are not present?", "It is usually caused by Nitrogen deficiency (if nodules fail to form), or Iron deficiency in highly alkaline soils.", "Fertilizer Management"),
    ("How does over-fertilization with Urea affect bean plants?", "Excess Nitrogen promotes massive leafy vegetative growth at the expense of flowers and pods, drastically reducing the actual vegetable yield.", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("How should beans be irrigated?", "Beans should be irrigated lightly but frequently. The soil must remain moist, but water should never stand in the field.", "Irrigation & Weeds"),
    ("What happens if a bean field is waterlogged?", "Standing water cuts off oxygen to the roots, causing the plants to turn yellow and succumb to fungal root rots within 24 to 48 hours.", "Irrigation & Weeds"),
    ("What is the most critical stage for irrigation in beans?", "The flowering and pod-filling stages are the most critical. Drought stress during this time causes massive flower shedding and malformed, stringy pods.", "Irrigation & Weeds"),
    ("How are weeds controlled in bean fields?", "Manual hoeing (Godi) is the best method, done 20-25 days after sowing. Pre-emergence herbicides like Pendimethalin can also be sprayed immediately after sowing.", "Irrigation & Weeds"),
    ("Why is manual hoeing highly beneficial for beans?", "It not only removes weeds but also breaks the soil crust, allowing better aeration for the roots and nitrogen-fixing nodules.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("What damage do aphids cause in French beans?", "Aphids cluster on young shoots and under leaves, sucking sap. This stunts growth, curls the leaves, and secretes sticky honeydew that causes sooty mold.", "Pest Management"),
    ("How to control aphids in French beans?", "Spray systemic insecticides like Imidacloprid, Thiamethoxam, or Flonicamid as soon as aphid clusters are observed.", "Pest Management"),
    ("How does the whitefly damage bean crops?", "Whiteflies suck sap and transmit viral diseases like the Yellow Mosaic Virus. Control them with Pyriproxyfen (for nymphs) or Diafenthiuron (for adults).", "Pest Management"),
    ("What is the Pod Borer (Helicoverpa) and how does it damage beans?", "The pod borer caterpillar drills holes into the bean pods and eats the developing seeds, making the pods entirely unmarketable.", "Pest Management"),
    ("How to control pod borers in beans?", "Spray Emamectin Benzoate, Lufenuron, or Chlorantraniliprole (Coragen) during the flowering and early pod-formation stages.", "Pest Management"),
    ("How to manage red ants in the bean field?", "Red ants can carry away sown seeds or attack young roots. Dusting the field boundaries with Carbaryl or flushing Chlorpyrifos with irrigation controls them.", "Pest Management"),
    ("What are hairy caterpillars in Dolichos beans?", "These are highly destructive, fuzzy caterpillars that voraciously eat the foliage. They can be controlled by spraying Emamectin Benzoate or Match.", "Pest Management"),
    ("How to control leaf miners in beans?", "Leaf miners create white, winding trails inside the leaves. Spraying Abamectin or Spinetoram effectively controls them.", "Pest Management"),
    ("How to protect beans from spider mites during dry periods?", "Spider mites cause leaves to look stippled and yellow, often with fine webbing. Spray an acaricide like Abamectin or Chlorfenapyr.", "Pest Management"),

    # --- Disease Management ---
    ("What causes Root Rot in French beans and how is it managed?", "It is caused by soil-borne fungi (Rhizoctonia/Fusarium) thriving in overly wet soil. Manage it by planting on ridges, avoiding over-irrigation, and treating seeds with Thiophanate-methyl.", "Disease Management"),
    ("How to control Fungal Wilt in beans?", "Fungal wilt causes sudden drooping and drying of the plant. Drench the soil around the affected plants with Carbendazim or Thiophanate-methyl.", "Disease Management"),
    ("What is Leaf Spot disease in beans?", "Leaf spot appears as circular brown or black necrotic spots on leaves. It spreads rapidly in humid weather.", "Disease Management"),
    ("How to control Leaf Spot disease?", "Spray broad-spectrum protectant fungicides like Mancozeb (Indofil M-45) or Chlorothalonil before the disease spreads.", "Disease Management"),
    ("What is Mungbean Yellow Mosaic Virus (MYMV) and does it affect other beans?", "Yes, it affects many legumes, causing the leaves to turn bright yellow with green patches. It is transmitted by whiteflies.", "Disease Management"),
    ("How to control viral diseases in beans?", "Viruses cannot be cured chemically. The only control is to immediately uproot and burn infected plants and aggressively spray insecticides to kill the whitefly vector.", "Disease Management"),
    ("What causes Powdery Mildew on beans?", "A fungus that forms a white powdery coating on leaves and stems during cool, humid nights. Controlled by spraying Sulphur-based fungicides or Difenoconazole.", "Disease Management"),

    # --- Harvesting, Storage & FAQs ---
    ("When should vegetable beans be harvested?", "Pods should be harvested while they are young, tender, and the internal seeds are small. Over-matured pods become tough, fibrous, and stringy.", "Harvesting & Storage"),
    ("How frequently should beans be picked?", "For continuous production, picking should be done every 3 to 4 days. Regular picking stimulates the plant to produce more flowers.", "Harvesting & Storage"),
    ("What is the average yield of French beans per acre?", "With good management, a yield of 4000 to 5000 kg of fresh green pods per acre can be achieved.", "FAQs"),
    ("How should fresh beans be stored post-harvest?", "Fresh beans lose moisture rapidly. They should be kept in a cool, shaded place and transported to the market immediately. In cold storage, they can be kept at 5-7°C for a week.", "FAQs"),
    ("Why do prices of French beans fluctuate so much in Pakistan?", "Prices peak during peak summer and peak winter when plains cannot grow them. Prices drop in spring and autumn when the local harvest from Punjab/Sindh floods the market.", "FAQs"),
    ("What is the nutritional value of French beans?", "They are highly nutritious, providing excellent dietary fiber, Vitamin A, Vitamin C, Iron, and a good amount of plant-based protein.", "FAQs"),
    ("Can the dried seeds of French beans be consumed?", "Yes, if the pods are left to mature and dry on the plant, the seeds can be harvested and used as dry beans (like Rajma/Kidney beans).", "FAQs"),
    ("What is trellis farming and why is it used for Yard Long beans?", "Trellising involves erecting bamboo sticks and wires to support climbing beans. It keeps the pods off the ground, preventing rotting and making harvesting much easier.", "FAQs"),
    # --- Advanced Bean Agronomy & Pathology ---
    ("What is Rhizobium inoculation in beans?", "Coating bean seeds with Rhizobium leguminosarum bacteria before sowing allows the roots to form nodules that fix atmospheric nitrogen, drastically reducing the need for Urea fertilizer.", "Advanced Agronomy"),
    ("What causes 'Hard Seed' phenomenon in stored beans?", "Storing beans in very hot, dry conditions causes the seed coat to become impermeable to water. When cooked or planted, these hard seeds fail to absorb water and remain rock hard.", "Harvest & Post-Harvest"),
    ("What is Anthracnose in bean crops?", "Anthracnose is a devastating seed-borne fungal disease causing sunken, dark brown, water-soaked lesions on the pods, stems, and leaves, favored by cool, wet weather.", "Disease Management"),
    ("How is Bean Halo Blight identified?", "Halo blight is a bacterial disease causing small brown spots on the leaves surrounded by a wide, distinct yellow 'halo'. It spreads rapidly via rain splash.", "Disease Management"),
    ("Why must mechanical threshers be run at very low RPMs for beans?", "Bean seeds are highly susceptible to mechanical damage. High thresher speeds crack the seed coat and split the cotyledons, ruining their germination capacity and market value.", "Harvest & Post-Harvest")
]

filename = 'Pakistan_Bean_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality bean queries successfully!")
