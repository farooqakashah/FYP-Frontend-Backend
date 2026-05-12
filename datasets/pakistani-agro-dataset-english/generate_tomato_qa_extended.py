import csv

qa_data = [
    # --- Nursery Raising & Transplanting ---
    ("What is the best soil type for cultivating tomatoes?", "Tomatoes grow best in well-drained sandy loam to clay loam soils rich in organic matter, with a pH of 6.0 to 7.0.", "Nursery & Transplanting"),
    ("How is a tomato nursery prepared?", "Seeds are sown on raised beds (4-5 inches high) to ensure drainage. The soil should be finely pulverized and mixed with well-rotted FYM and sand.", "Nursery & Transplanting"),
    ("What is the seed rate required for one acre of tomato?", "For hybrid varieties, 40 to 60 grams of seed is sufficient per acre. For open-pollinated (local) varieties, 100 to 120 grams are required.", "Nursery & Transplanting"),
    ("Why is seed treatment important for tomatoes?", "Treating seeds with a fungicide (like Thiram or Captan) prevents soil-borne diseases like 'Damping Off', which kills seedlings before or just after emergence.", "Nursery & Transplanting"),
    ("What causes 'Damping Off' in the tomato nursery?", "It is a fungal disease caused by excessive moisture, overcrowding of seedlings, and poor drainage in the nursery beds.", "Nursery & Transplanting"),
    ("At what stage should tomato seedlings be transplanted?", "Seedlings should be transplanted when they are 4 to 5 weeks old, having 4-6 true leaves and a height of 10-15 cm.", "Nursery & Transplanting"),
    ("What is the optimal spacing for transplanting tomatoes?", "For indeterminate (climbing) varieties, the row-to-row spacing is 3-4 feet and plant-to-plant is 1.5-2 feet. For determinate (bushy) varieties, spacing can be slightly closer.", "Nursery & Transplanting"),

    # --- Varieties & Growth Habits ---
    ("What is the difference between determinate and indeterminate tomatoes?", "Determinate varieties grow to a fixed bush size and bear fruit all at once (good for open field). Indeterminate varieties grow like vines continuously and produce fruit over a long season (good for tunnels/greenhouses).", "Varieties & Growth"),
    ("What are some popular determinate/open-field tomato varieties in Pakistan?", "Popular open-pollinated varieties include Rio Grande, Roma, and Nagina. They are preferred for their hardiness and suitability for processing/paste.", "Varieties & Growth"),
    ("What are some popular hybrid tomato varieties grown in Pakistan?", "Hybrids like Sahil, T-1359, Bella, and Ahmar are highly popular, especially in tunnel farming, due to their massive yields and disease resistance.", "Varieties & Growth"),

    # --- Provincial: Punjab ---
    ("When are tomatoes traditionally sown in the plains of Punjab?", "In Punjab, the spring crop is sown in nursery in November and transplanted in February. The autumn crop is sown in July and transplanted in August.", "Provincial: Punjab"),
    ("Why is 'Tunnel Farming' extremely popular for tomatoes in Punjab?", "Walk-in tunnels allow farmers to plant tomatoes in November, protecting them from winter frost, and bringing the harvest to market in early spring when prices are exceptionally high.", "Provincial: Punjab"),
    ("What are the major tomato-producing districts in Punjab?", "Sheikhupura, Gujranwala, Faisalabad, Sahiwal, and Vehari are major hubs for both open-field and tunnel-grown tomatoes.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("When are tomatoes cultivated in Sindh?", "Due to the warmer, frost-free winters in lower Sindh, tomatoes are primarily grown as a winter crop. Nursery is sown in August-September, and transplanting occurs in October.", "Provincial: Sindh"),
    ("What are the leading tomato-producing districts in Sindh?", "Thatta, Badin, Mirpurkhas, and Hyderabad are the leading districts, supplying the entire country during the winter months.", "Provincial: Sindh"),
    ("What is the main challenge for tomato farmers in Sindh?", "High salinity, water shortages in specific canals, and early heat waves in March that abruptly end the harvesting season.", "Provincial: Sindh"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("What role does KPK play in the national tomato supply?", "The cooler, mountainous regions of KPK (like Swat and Dir) produce tomatoes during the peak summer months (July-September) when the plains are too hot to grow them.", "Provincial: KPK"),
    ("What is the sowing time for tomatoes in the hilly areas of KPK?", "Nursery is sown in March-April, and transplanting is done in May. The crop is harvested throughout late summer and autumn.", "Provincial: KPK"),

    # --- Provincial: Balochistan ---
    ("Why is Balochistan's tomato crop economically significant?", "Balochistan supplies tomatoes during late summer and autumn (August-November) from highland areas like Kalat, Mastung, and Quetta, commanding premium prices.", "Provincial: Balochistan"),
    ("How are tomatoes cultivated in the arid regions of Balochistan?", "Farmers heavily rely on groundwater (tube wells) and increasingly adopt drip irrigation to maximize water efficiency in the arid climate.", "Provincial: Balochistan"),

    # --- Fertilizer, Irrigation & Pruning ---
    ("What is the general fertilizer recommendation for an acre of tomatoes?", "Apply 1-2 bags of DAP, 2 bags of Urea, and 1-2 bags of SOP/Potash. Potash is critical for fruit size, weight, and color.", "Agronomy"),
    ("How should tomatoes be irrigated in open fields?", "Tomatoes should be irrigated via furrows. Water should never touch the main stem or leaves to avoid soil-borne fungal diseases like collar rot.", "Agronomy"),
    ("Why is Drip Irrigation highly recommended for tomatoes?", "Drip irrigation saves up to 50% water, prevents weed growth, reduces fungal diseases (by keeping foliage dry), and allows precise application of fertilizers (fertigation).", "Agronomy"),
    ("What causes Blossom End Rot (BER) in tomatoes?", "BER is a physiological disorder where the bottom of the tomato turns black and sunken. It is caused by Calcium deficiency and irregular watering.", "Agronomy"),
    ("What is 'Staking' in tomato farming?", "Staking involves tying the tomato plant to wooden or bamboo sticks. It keeps the fruit off the wet ground, preventing rotting and making harvesting easier.", "Agronomy"),
    ("Why is pruning important for indeterminate tomatoes in tunnels?", "Pruning (removing side shoots or 'suckers') directs the plant's energy into the main stem and fruit production, rather than excessive leafy growth. It also improves air circulation.", "Agronomy"),

    # --- Pest Management ---
    ("What is the Tomato Fruit Borer (Helicoverpa) and how to manage it?", "The fruit borer caterpillar drills holes into the green/ripe fruit, making it unmarketable. Spray Emamectin Benzoate, Flubendiamide, or Lufenuron during flowering/fruiting.", "Pest Management"),
    ("How does the Whitefly damage tomato crops?", "Whiteflies suck sap from the leaves, weakening the plant. More critically, they are the sole vector for transmitting the deadly Tomato Leaf Curl Virus.", "Pest Management"),
    ("How to control Whitefly infestations?", "Rotate chemistries: use Diafenthiuron, Pyriproxyfen, or Flonicamid. Use yellow sticky traps in greenhouses for early detection and mass trapping.", "Pest Management"),
    ("What damage do Thrips cause to tomatoes?", "Thrips scrape the leaves and flowers, causing them to curl upwards and develop a silvery sheen. They also transmit Spotted Wilt Virus. Spray Spinetoram or Chlorfenapyr.", "Pest Management"),
    ("How to control Aphids in tomatoes?", "Aphids cluster on young shoots, stunting growth and secreting sticky honeydew. Spray systemic insecticides like Imidacloprid or Acetamiprid.", "Pest Management"),
    ("What are Leaf Miners and how to control them?", "Leaf miners are tiny larvae that tunnel inside the leaf tissue, creating white zig-zag trails. Spray Abamectin or Spinetoram to control them.", "Pest Management"),

    # --- Disease Management ---
    ("What is Tomato Leaf Curl Virus (TLCV) and how to manage it?", "TLCV is the most devastating disease, causing severe upward leaf curling, stunting, and complete loss of yield. It has no chemical cure; control the whitefly vector and use resistant hybrids.", "Disease Management"),
    ("What is Late Blight of tomato?", "A highly destructive fungal disease that spreads rapidly in cool, wet weather. It causes large water-soaked, dark spots on leaves, stems, and fruits.", "Disease Management"),
    ("How to manage Early Blight and Late Blight?", "Avoid overhead watering. Spray protectant fungicides like Mancozeb (Indofil M-45) early. If infection occurs, use curative systemic fungicides like Metalaxyl or Cymoxanil.", "Disease Management"),
    ("What causes Bacterial Wilt in tomatoes?", "Bacterial wilt causes healthy, green plants to suddenly wilt and die without yellowing. Slicing the stem near the base reveals brown discoloration and milky ooze.", "Disease Management"),
    ("How to control Bacterial Wilt?", "There is no chemical cure. The only management is to immediately uproot and burn infected plants, use disease-free seed, and practice a 3-year crop rotation.", "Disease Management"),
    ("What is Fusarium Wilt (Fungal Wilt) and how is it controlled?", "It causes gradual yellowing and wilting of the plant starting from the lower leaves. Treat seeds with fungicides and apply a soil drench of Thiophanate-methyl.", "Disease Management"),
    ("How does heavy rain affect the tomato crop?", "Heavy rain causes physical damage to flowers, splits mature fruits, washes away pesticides, and creates perfect humid conditions for blight and wilting diseases.", "Disease Management"),

    # --- Harvesting, Storage & Processing ---
    ("When should tomatoes be harvested for long-distance transport?", "They should be harvested at the 'Breaker Stage' (when a pink/yellow star appears at the blossom end) or the 'Pink Stage'. They will ripen during transport.", "Harvest & Post-Harvest"),
    ("When should tomatoes be harvested for local markets or processing?", "They should be harvested at the 'Red Ripe' stage for maximum flavor, color, and weight.", "Harvest & Post-Harvest"),
    ("Why do tomato prices experience extreme fluctuations in Pakistan?", "Prices crash during peak harvests (spring in Punjab, winter in Sindh) due to oversupply. Prices skyrocket in late summer/autumn when only highland areas (KPK/Balochistan) produce them.", "Harvest & Post-Harvest"),
    ("How long can fresh tomatoes be stored?", "Mature green tomatoes can be stored at 12-15°C for 2-3 weeks. Fully ripe tomatoes have a very short shelf life of a few days at room temperature.", "Harvest & Post-Harvest"),
    ("Why is chilling injury a concern during storage?", "Storing tomatoes in a standard refrigerator (below 10°C) permanently halts the ripening process, destroys the flavor-producing enzymes, and makes the flesh mealy.", "Harvest & Post-Harvest"),
    ("What is the role of the tomato processing industry in Pakistan?", "Processing factories purchase bulk quantities of Roma/determinate tomatoes during glut periods to make tomato paste, ketchup, and puree, which helps stabilize market prices.", "Harvest & Post-Harvest"),
    # --- Advanced Tomato Horticulture & Tunnels ---
    ("Why are tomatoes grafted onto wild eggplant rootstocks?", "Grafting high-yielding tomato scions onto wild eggplant rootstocks provides immense resistance against soil-borne diseases like Bacterial Wilt and Root-Knot Nematodes, which devastate non-grafted tomatoes.", "Advanced Horticulture"),
    ("What is the Tuta absoluta crisis in tomatoes?", "Tuta absoluta is an incredibly destructive, invasive leafminer moth. The larvae mine into leaves, stems, and fruits. It is highly resistant to chemicals and requires pheromone mass-trapping.", "Pest Management"),
    ("Why is ventilation critical in tunnel/polyhouse tomato farming?", "Poor ventilation traps humidity, creating the perfect microclimate for Botrytis (Grey Mold) and Late Blight to destroy the entire crop in days.", "Advanced Horticulture"),
    ("What causes 'Blossom Drop' during the Pakistani summer?", "When daytime temperatures exceed 35°C and nights remain hot, tomato pollen becomes sterile. The unpollinated flowers simply dry up and drop off without setting any fruit.", "Physiological Disorders"),
    ("What is Blossom End Rot (BER) and how is it corrected?", "BER is a dark, leathery, sunken spot at the bottom of the tomato fruit. It is caused by localized Calcium deficiency, usually triggered by irregular watering (drought stress) rather than actual lack of soil calcium.", "Physiological Disorders"),
    ("How is 'Staking' mathematically linked to higher tomato yields?", "Staking (supporting vines on vertical trellises/strings) keeps foliage off the wet ground (preventing rot), maximizes leaf exposure to sunlight for photosynthesis, and allows high-density planting in tunnels.", "Advanced Horticulture")
]

filename = 'Pakistan_Tomato_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality tomato queries successfully!")
