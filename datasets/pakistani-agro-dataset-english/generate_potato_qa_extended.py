import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What kind of soil is most suitable for potato cultivation?", "Potato requires well-drained, deep, and friable loamy or sandy loam soil. Heavy clay soils restrict tuber expansion and promote rotting.", "Field Preparation"),
    ("Why is deep ploughing necessary for potato?", "Deep ploughing (using a chisel or moldboard plow) followed by rotavator creates a fine tilth, which is essential for proper root development and unrestricted tuber growth.", "Field Preparation"),
    ("What is the recommended row-to-row distance for potato?", "The recommended row-to-row distance is 2.5 feet (75 cm) on ridges.", "Field Preparation"),
    ("What is the recommended plant-to-plant distance?", "The plant-to-plant distance should be kept between 8 to 10 inches (20-25 cm) depending on the seed size.", "Field Preparation"),
    ("How much Farm Yard Manure (FYM) is needed for potato?", "Apply 10-12 trolleys (20-25 tons) of well-rotted Farm Yard Manure per acre at least one month before sowing to increase soil organic matter.", "Field Preparation"),
    ("Can potatoes be grown on flat land without ridges?", "It is not recommended. Planting on ridges prevents water from touching the plant stems, reducing the risk of fungal rots, and makes harvesting easier.", "Field Preparation"),
    ("When and how is 'earthing up' (Mitti charhana) done?", "Earthing up is done 30-40 days after sowing. Soil from the furrows is pulled up to cover the base of the plant.", "Field Preparation"),
    ("Why is earthing up important in potato cultivation?", "It provides space for tuber expansion, covers exposed tubers (which turn green and poisonous if exposed to sunlight), and supports the plant against lodging.", "Field Preparation"),
    ("What is the ideal seed depth for planting potatoes?", "Seed tubers should be planted at a depth of 3 to 4 inches inside the ridge.", "Field Preparation"),
    ("What happens if potatoes are planted too deep?", "Deep planting delays emergence, reduces plant vigor, and makes harvesting difficult and prone to tuber damage.", "Field Preparation"),

    # --- Seed Selection & Treatment ---
    ("What is the ideal seed rate for planting one acre of potato?", "Depending on tuber size, approximately 1000 to 1200 kg (25-30 maunds) of seed is required per acre.", "Seed Selection & Treatment"),
    ("What is the ideal tuber size for seed?", "Medium-sized tubers, about the size of a hen's egg (35-50 grams), are ideal for planting.", "Seed Selection & Treatment"),
    ("Can large potato tubers be cut and planted?", "Yes, large tubers can be cut into pieces. Each piece must have at least 2-3 healthy eyes (sprouts).", "Seed Selection & Treatment"),
    ("What precautions should be taken when planting cut tubers?", "Cut pieces should be treated with a fungicide and kept in a cool, shaded place for 24-48 hours to heal (suberize) before planting to prevent rotting.", "Seed Selection & Treatment"),
    ("How should whole seed potatoes be treated before sowing?", "According to expert recommendations, mix 5 gm of Indofil M-45 (Mancozeb) in 1 liter of water. Dip the seeds for 10 minutes and shade-dry for 48 hours.", "Seed Selection & Treatment"),
    ("Why is seed treatment critical for potatoes?", "It protects the tubers from seed-borne and soil-borne diseases such as late blight, early blight, black scurf, and common scab during early growth.", "Seed Selection & Treatment"),
    ("What is seed 'chitting' or sprouting?", "Chitting is the process of encouraging seed potatoes to sprout before planting by keeping them in diffused light at 15-20°C. It leads to faster field emergence.", "Seed Selection & Treatment"),
    ("Why should farmers avoid using uncertified, local bazaar potatoes as seed?", "Table potatoes from the market are often infected with invisible viruses (like Potato Leaf Roll Virus), which can drastically reduce yield.", "Seed Selection & Treatment"),
    ("What is physiological age in seed potatoes?", "It refers to the stage of the tuber. Seed with a single, long sprout is too old, while seed with multiple short, thick sprouts is ideal.", "Seed Selection & Treatment"),
    ("Should I plant seed potatoes directly after removing them from cold storage?", "No, seeds should be kept in a shaded, well-ventilated area for 7-10 days to break dormancy and develop small sprouts before planting.", "Seed Selection & Treatment"),

    # --- Varieties of Pakistan ---
    ("What are the most popular red-skinned potato varieties in Pakistan?", "Popular red-skinned varieties include Desiree, Cardinal, Kuroda, and Rocco.", "Varieties"),
    ("What are the most popular white/yellow-skinned varieties in Pakistan?", "Popular white/yellow varieties include Sante, Diamant, Hermes, Faisalabad White, and Mozika.", "Varieties"),
    ("Which potato varieties are best for making French fries?", "Sante, Hermes, and Diamant are preferred for fries due to their shape and optimal dry matter content.", "Varieties"),
    ("Which potato varieties are best suited for making chips (crisps)?", "Lady Rosetta (LR) and Hermes are highly demanded by the processing industry for chips because of their high dry matter and low reducing sugars.", "Varieties"),
    ("Is 'Kufri Chandramukhi' recommended for cultivation in Pakistan?", "No, Kufri Chandramukhi is an Indian variety. Farmers in Pakistan should instead cultivate localized equivalents like Faisalabad White or Sante for better adaptability.", "Varieties"),
    ("What is the specialty of the 'Kuroda' variety?", "Kuroda is a red-skinned variety known for its attractive color, high yield, and good market acceptance in Pakistan.", "Varieties"),
    ("Why is the 'Desiree' variety so common among small farmers?", "Desiree has high adaptability, tolerates drought stress relatively well, and has excellent cooking qualities, making it a reliable choice.", "Varieties"),

    # --- Provincial: Punjab ---
    ("Which province is the largest producer of potatoes in Pakistan?", "Punjab produces over 95% of Pakistan's total potato crop.", "Provincial: Punjab"),
    ("What are the core potato-producing districts in Punjab?", "The core districts are Okara, Sahiwal, Kasur, Pakpattan, and parts of Chiniot and Jhang.", "Provincial: Punjab"),
    ("How many potato crops are grown annually in Punjab?", "Three crops are grown: Autumn (main crop), Spring, and Summer (in hilly areas like Murree).", "Provincial: Punjab"),
    ("What is the sowing and harvesting time for the Autumn potato crop in Punjab?", "The Autumn crop is sown from mid-September to mid-October and harvested from January to February.", "Provincial: Punjab"),
    ("What is the sowing and harvesting time for the Spring potato crop in Punjab?", "The Spring crop is sown from January to mid-February and harvested in May.", "Provincial: Punjab"),
    ("Why is the Autumn crop the most important in Punjab?", "The Autumn crop accounts for 75-80% of total production, provides the seed for the Spring crop, and is highly suitable for cold storage and export.", "Provincial: Punjab"),
    ("What is the main challenge for the Spring crop in Punjab?", "The rapid rise in temperature in April and May limits tuber expansion and increases the threat of sucking pests and viral diseases.", "Provincial: Punjab"),
    ("How does frost affect the Autumn crop in Punjab?", "Severe frost in late December or January damages the foliage. Applying light irrigation before expected frost helps protect the crop.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("When is potato cultivated in Sindh?", "In Sindh, potato is primarily grown as a single winter crop.", "Provincial: Sindh"),
    ("What is the optimal sowing time for potato in Sindh?", "Sowing is done slightly later than Punjab, typically from late October to November, when temperatures become favorable.", "Provincial: Sindh"),
    ("Which districts in Sindh are known for potato cultivation?", "Khairpur, Shikarpur, Sukkur, and Naushahro Feroze are the main potato-producing districts.", "Provincial: Sindh"),
    ("What is a major climatic challenge for potato farmers in Sindh?", "The shorter, milder winter season limits the vegetative growth period, requiring early-maturing varieties to achieve good yields.", "Provincial: Sindh"),
    ("Are red or white potatoes preferred in Sindh?", "Both are grown, but white varieties often have strong market demand in the southern region.", "Provincial: Sindh"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("In which seasons is potato grown in KPK?", "KPK grows potato in the plains during winter/spring and in the northern mountainous regions during summer.", "Provincial: KPK"),
    ("What is the sowing and harvesting time for the summer crop in hilly areas of KPK?", "In areas like Swat, Dir, and Kaghan, potatoes are sown in April-May and harvested in September-October.", "Provincial: KPK"),
    ("What role do the hilly areas of KPK play in seed production?", "The high-altitude regions (above 2000m) are ideal for producing virus-free certified seed potatoes because of the absence of aphid vectors.", "Provincial: KPK"),
    ("What are the main potato-producing districts in KPK?", "Swat, Dir, Mansehra, Abbottabad, and Nowshera are significant producers.", "Provincial: KPK"),
    ("How does the summer crop of KPK benefit the national market?", "It supplies fresh potatoes to the country during late summer and autumn when the plains only have cold-storage stock.", "Provincial: KPK"),

    # --- Provincial: Balochistan ---
    ("Where is potato primarily cultivated in Balochistan?", "It is cultivated in the highland valleys of Kalat, Pishin, Ziarat, and Quetta.", "Provincial: Balochistan"),
    ("What is the cropping season for potatoes in highland Balochistan?", "It is grown as a summer crop. Sowing is done in April-May, and the crop is harvested from August to October.", "Provincial: Balochistan"),
    ("Why is Balochistan's potato crop economically important?", "It reaches the national markets during the off-season (August-October), fetching premium prices for farmers.", "Provincial: Balochistan"),
    ("What is a major constraint for potato farming in Balochistan?", "Water scarcity and lack of modern cold storage infrastructure are the biggest challenges.", "Provincial: Balochistan"),
    ("Which varieties perform well in Balochistan?", "Drought-tolerant and adaptable varieties like Desiree and Cardinal perform very well in Balochistan's arid highlands.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the general recommended NPK fertilizer dose for irrigated potato?", "Apply 2 bags of DAP, 2-3 bags of Urea, and 1-2 bags of SOP (Sulphate of Potash) per acre.", "Fertilizer Management"),
    ("When should DAP be applied?", "The entire dose of DAP (Phosphorus) must be applied as a basal dose at the time of field preparation/sowing.", "Fertilizer Management"),
    ("How should Urea be applied to the potato crop?", "Urea should be split: half at sowing or first irrigation, and the remaining half at the time of earthing up (30-40 days after sowing).", "Fertilizer Management"),
    ("Why is Potash (SOP) critical for potatoes?", "Potash significantly increases tuber size, improves skin finish, enhances dry matter content, and increases resistance to frost and diseases.", "Fertilizer Management"),
    ("Can MOP (Muriate of Potash) be used instead of SOP?", "No, avoid MOP because it contains chloride, which reduces the specific gravity and cooking quality of the potatoes.", "Fertilizer Management"),
    ("When should micronutrients be applied to potatoes?", "Micronutrient cocktails (Zinc, Boron, Iron) should be applied as foliar sprays 30-45 days after planting.", "Fertilizer Management"),
    ("What causes chlorosis (yellowing of young leaves) in potato?", "It is primarily caused by Iron or Nitrogen deficiency. A foliar spray of 1% Ferrous Sulphate or Urea can resolve it quickly.", "Fertilizer Management"),
    ("How to address Zinc deficiency in potato?", "Zinc deficiency causes stunted plants and 'fern-like' leaves. Apply 10 kg of 33% Zinc Sulphate to the soil during early irrigations.", "Fertilizer Management"),
    ("What is the role of Boron in potato cultivation?", "Boron prevents internal cracking (hollow heart) in tubers and improves the translocation of sugars to the tubers.", "Fertilizer Management"),
    ("How to manage poor overall growth in the potato field?", "Ensure soil is not waterlogged, apply a balanced NPK fertilizer, and use a bio-stimulant or amino acid foliar spray to relieve stress.", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("What is the first irrigation schedule for potatoes?", "The first irrigation must be given immediately after planting, ensuring the water does not rise above 2/3rd the height of the ridges.", "Irrigation & Weeds"),
    ("How frequently should potato be irrigated?", "Depending on soil type, irrigate every 7-10 days. The soil must remain moist but never waterlogged.", "Irrigation & Weeds"),
    ("What happens if water crosses the top of the ridge?", "It forms a hard crust, suffocates the emerging sprouts, and creates a highly favorable environment for tuber rotting diseases.", "Irrigation & Weeds"),
    ("When should irrigation be stopped before harvesting?", "Stop irrigation 10 to 15 days before harvest to allow the tuber skin to mature and toughen.", "Irrigation & Weeds"),
    ("What are the major weeds in the potato crop?", "Common weeds include Bathu (Chenopodium), Dumbi Sitti (Phalaris minor), and Itsit (Trianthema).", "Irrigation & Weeds"),
    ("What pre-emergence herbicide is recommended for potato?", "Spray Pendimethalin or Metribuzin (Sencor) within 24-48 hours of the first irrigation to prevent weed germination.", "Irrigation & Weeds"),
    ("Is Metribuzin safe for all potato varieties?", "No, some varieties are sensitive to Metribuzin. Always check variety tolerance or use Pendimethalin as a safer alternative.", "Irrigation & Weeds"),
    ("Can weeds be controlled manually in potatoes?", "Yes, manual hoeing before earthing up is highly beneficial as it removes weeds and aerates the roots simultaneously.", "Irrigation & Weeds"),
    ("How does drought stress at the tuber initiation stage affect the crop?", "It drastically reduces the number of tubers per plant, leading to a massive drop in final yield.", "Irrigation & Weeds"),
    ("How does waterlogging affect the potato crop?", "Potatoes are highly sensitive to waterlogging. Standing water for more than 24 hours causes oxygen starvation, wilting, and severe rotting.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("How to control termite attacks in the potato field?", "Treat the soil with Chlorpyrifos or Fipronil before sowing. If attacked later, flush Chlorpyrifos with the irrigation water.", "Pest Management"),
    ("What damage do cutworms cause and how to control them?", "Cutworms cut young seedlings at the base during the night. Spray Emamectin Benzoate or Chlorpyrifos at the base of the plants in the evening.", "Pest Management"),
    ("How to control red ants in potato cultivation?", "Red ants can damage seeds and roots. Dusting the field with Carbaryl or flushing Fipronil with irrigation controls them.", "Pest Management"),
    ("What is the damage caused by aphids in potato?", "Aphids suck plant sap causing weakness, but more dangerously, they transmit viral diseases like the Potato Leaf Roll Virus (PLRV).", "Pest Management"),
    ("How to control aphids and whiteflies?", "Spray systemic insecticides like Imidacloprid, Thiamethoxam, Flonicamid, or Acetamiprid as soon as the pest is sighted.", "Pest Management"),
    ("How to identify and control leaf miners in potato?", "Leaf miners create white, zig-zag tunnels inside the leaves. Spray systemic chemicals like Abamectin or Emamectin Benzoate.", "Pest Management"),
    ("What are leaf-eating caterpillars in potato and how to manage them?", "Armyworms and loopers eat the foliage rapidly. Spray Emamectin Benzoate, Lufenuron, or Match to control them.", "Pest Management"),
    ("What are root-knot nematodes and how do they affect potatoes?", "Nematodes cause small gall-like bumps on roots and tubers, reducing market value. Practice crop rotation with cereals and use nematicides like Carbofuran.", "Pest Management"),
    ("How to protect stored potatoes from the Potato Tuber Moth?", "Store in clean facilities. In local storage, cover tubers with a 1-inch layer of dry sand or neem leaves. Cold storage naturally suppresses the moth.", "Pest Management"),
    ("How to control jassids (leafhoppers) in potatoes?", "Jassids cause hopper burn (yellowing and curling of leaf edges). Spray Imidacloprid or Nitenpyram.", "Pest Management"),
    ("Why should excessive nitrogen be avoided for pest control?", "Too much Urea makes the plant succulent, heavily attracting sucking pests like aphids and whiteflies.", "Pest Management"),
    ("Are there any beneficial insects in the potato field?", "Yes, ladybird beetles aggressively feed on aphids. Avoid broad-spectrum insecticides if ladybird populations are high.", "Pest Management"),

    # --- Disease Management ---
    ("What is Late Blight disease and what are its symptoms?", "Late blight is the most destructive potato disease. Symptoms include large water-soaked, dark brown spots on leaves that rapidly spread in cool, humid weather.", "Disease Management"),
    ("What is the preventive control for Late Blight?", "Treat seed tubers with Indofil M-45 (Mancozeb) @ 5g/L. Also, apply a preventive foliar spray of Mancozeb before the weather turns cool and foggy.", "Disease Management"),
    ("How to control Late Blight once it infects the standing crop?", "Spray systemic and curative fungicides like Metalaxyl + Mancozeb, Cymoxanil, or Dimethomorph immediately.", "Disease Management"),
    ("What is Early Blight and how is it managed?", "It causes small brown spots with concentric rings (target-board appearance) on older leaves. Control it by spraying Chlorothalonil or Propineb.", "Disease Management"),
    ("What causes Bacterial Wilt in potato?", "It is caused by soil-borne bacteria resulting in sudden wilting of green, healthy-looking plants. Slicing the stem reveals a milky bacterial ooze.", "Disease Management"),
    ("How to control Bacterial Wilt?", "There is no chemical cure. Use strictly certified disease-free seed, uproot and burn infected plants, and practice a 3-year crop rotation.", "Disease Management"),
    ("What is Potato Leaf Roll Virus (PLRV)?", "It is a viral disease that causes leaves to roll upward, become stiff, and turn pale. It is spread by aphids.", "Disease Management"),
    ("How to manage Leaf Curl / PLRV in potatoes?", "Since viruses cannot be cured, prevention is the only way: Use virus-free seed and strictly control aphid populations with systemic insecticides.", "Disease Management"),
    ("What is Common Scab of potato?", "It is a bacterial infection causing rough, corky patches on the tuber skin, reducing its market value. It thrives in dry, alkaline soils.", "Disease Management"),
    ("How to prevent Common Scab?", "Maintain adequate soil moisture during tuber initiation, avoid excessive lime/ash, and treat seeds before planting.", "Disease Management"),
    ("How to manage fungal wilt or Fusarium wilt?", "Fungal wilt causes slow yellowing and drying of the plant. Treat seeds with fungicides and drench the soil with Thiophanate-methyl.", "Disease Management"),
    ("What causes Stem Rot or Collar Rot in potato?", "Soil-borne fungi attack the stem base in excessively wet conditions. Avoid over-irrigation and apply Carbendazim.", "Disease Management"),
    ("What is Black Scurf disease?", "Black scurf appears as hard, black, dirt-like masses on the tuber skin (sclerotia). It is prevented by treating seeds with Fludioxonil or Pencycuron.", "Disease Management"),
    ("What is Damping Off in potato nurseries/TPS?", "Damping off kills young seedlings at the soil line. It is controlled by avoiding excessive moisture and drenching with Metalaxyl.", "Disease Management"),
    ("What is soft rot in potato storage?", "A bacterial disease that turns tubers into a foul-smelling mush. Ensure tubers are dry, uninjured, and stored in well-ventilated areas to prevent it.", "Disease Management"),

    # --- Harvesting, Storage, & FAQs ---
    ("How to determine if the potato crop is ready for harvest?", "The crop is ready when the foliage turns yellow and dies, and the tuber skin becomes firm and cannot be easily rubbed off with a thumb.", "Harvesting & Storage"),
    ("What is 'haulm cutting' and why is it done?", "Cutting the aerial foliage (haulms) 10-15 days before harvest stops growth and thickens the tuber skin, improving storage life.", "Harvesting & Storage"),
    ("How should potatoes be handled during harvest?", "Harvest carefully to avoid cuts and bruises. Damaged tubers are highly susceptible to rotting during transport and storage.", "Harvesting & Storage"),
    ("What is 'curing' of harvested potatoes?", "Keep harvested potatoes in a shaded, well-ventilated place for a week. This allows minor cuts to heal and the skin to harden completely.", "Harvesting & Storage"),
    ("What is the optimal temperature for commercial cold storage of table potatoes?", "Table potatoes are stored at 3-4°C to prevent sprouting and minimize weight loss.", "Harvesting & Storage"),
    ("At what temperature should seed potatoes be stored?", "Seed potatoes are best stored at 2-4°C with 85-90% relative humidity.", "Harvesting & Storage"),
    ("Why do potatoes turn sweet in cold storage?", "Low temperatures (below 4°C) cause starches to convert into reducing sugars, making them taste sweet and turn dark brown when fried.", "Harvesting & Storage"),
    ("How to recondition sweet, cold-stored potatoes before frying?", "Keep them at room temperature (15-20°C) for 10-14 days. This reverses the process, converting sugars back to starch.", "Harvesting & Storage"),
    ("What is the average yield of potato per acre in Pakistan?", "The national average is around 80-100 bags (10-12 tons) per acre, but progressive farmers easily achieve 120-150 bags (15-18 tons).", "FAQs"),
    ("How does potato cultivation impact crop rotation?", "Potato is an excellent cash crop that fits well into crop rotations (e.g., Rice-Potato-Maize), improving overall farm income and soil fertility.", "FAQs"),
    ("Why do potato prices fluctuate drastically in Pakistan?", "Prices fluctuate due to the 'cobweb phenomenon'—high prices one year lead to overproduction the next year, causing a glut and crashing the market.", "FAQs"),
    ("How can farmers mitigate price risks in potato farming?", "Farmers should utilize cold storage facilities to hold their crop during glut periods and release it gradually when prices stabilize.", "FAQs"),
    ("What is True Potato Seed (TPS)?", "TPS refers to the actual botanical seeds extracted from the berries of the potato plant, used primarily for breeding or disease-free propagation.", "FAQs"),
    ("Is TPS cultivation common in Pakistan?", "No, commercial cultivation in Pakistan is almost entirely done using vegetative propagation (tubers).", "FAQs"),
    ("What causes hollow heart in potatoes?", "Hollow heart is an irregular cavity in the center of a large potato caused by erratic growth due to uneven watering or excessive nitrogen.", "FAQs"),
    # --- Advanced Seed Production: Tissue Culture & Aeroponics ---
    ("What is Tissue Culture in potato seed production?", "Tissue culture is a high-tech laboratory method used to clone potato plants from microscopic meristem tissue in a sterile environment, producing 100% virus-free and disease-free plantlets.", "Advanced Agronomy"),
    ("Why is Pakistan shifting towards Aeroponics for potato seed production?", "Aeroponics allows potato roots to hang in the air, intermittently sprayed with a nutrient mist. This method produces up to 10 times more mini-tubers per plant than soil methods, drastically reducing reliance on imported seeds.", "Advanced Agronomy"),
    ("What are the formal classes of potato seed in Pakistan?", "The formal seed chain progresses from Pre-basic (mini-tubers from tissue culture), to Basic (grown in screen houses), to Certified 1 and Certified 2 (multiplied in open fields and sold to farmers).", "Advanced Agronomy"),
    ("Why is imported potato seed from Holland so expensive?", "Imported seed (often variety 'Sante' or 'Desiree' from the Netherlands) carries huge freight costs, import duties, and certification premiums. It is completely virus-free, ensuring massive yields that offset the initial cost.", "Advanced Agronomy"),
    ("What is the 'Autumn to Autumn' seed cycle in Punjab?", "Farmers harvest the Autumn crop in February, place the small tubers in cold storage through the extreme summer heat, and then plant those same tubers as seed for the next Autumn crop in October.", "Advanced Agronomy"),

    # --- Advanced Machinery: Planters & Harvesters ---
    ("What is an Automatic Potato Planter?", "It is a tractor-drawn machine that automatically drops seed tubers at precise intervals, applies fertilizer, and constructs the soil ridge over the seed in a single pass.", "Machinery"),
    ("What happens if the planting cups on an automatic planter are too small?", "If the cups are smaller than the graded seed size, the machine will skip dropping seeds, leaving empty gaps in the field and severely reducing the overall plant population and yield.", "Machinery"),
    ("What is a Potato Digger (Spinner)?", "A digger is a simple PTO-driven machine that lifts the ridge, shakes the soil loose through a chain web, and drops the potatoes back onto the field surface for manual collection by laborers.", "Machinery"),
    ("What is the main drawback of using a fully automated Potato Harvester in Pakistan?", "Fully automated harvesters are very heavy, expensive, and require perfectly stone-free soils. They also cause significantly more bruising to the potato skin compared to manual collection behind a simple digger.", "Machinery"),

    # --- Deep Pathology: Nematodes & Complex Viruses ---
    ("What is the Potato Cyst Nematode (PCN) and why is it a quarantine threat?", "PCN (Globodera species) are microscopic worms that attack potato roots, forming visible cysts. They can survive in the soil for 20 years. Their presence can trigger international export bans.", "Disease Management"),
    ("How does Potato Virus Y (PVY) severely impact yield?", "PVY causes 'mosaic' patterns, leaf dropping, and severe stunting. A severe PVY infection can slash the total tuber yield by up to 80%. It is primarily transmitted by aphids.", "Disease Management"),
    ("What is 'Seed Degeneration'?", "It is the progressive build-up of viral diseases (like PVY and PVX) in potato tubers over successive generations, causing the crop yield to dramatically decline if a farmer replants their own seed year after year.", "Disease Management"),
    ("What causes Common Scab in potatoes?", "Common Scab is caused by the soil bacterium Streptomyces scabies. It creates rough, corky, unsightly lesions on the potato skin, severely reducing market value, though the inside remains edible.", "Disease Management"),
    ("How is Common Scab managed?", "The bacteria thrive in dry, alkaline soils. Management involves maintaining consistent soil moisture during tuber initiation and avoiding heavy applications of un-rotted, fresh Farm Yard Manure.", "Disease Management"),

    # --- Cold Storage Economics & Physiology ---
    ("What is Cold Induced Sweetening (CIS) in potatoes?", "When potatoes are stored at very low temperatures (below 4°C), the tuber's starch converts into reducing sugars. If these potatoes are fried, the sugars burn, turning the chips unacceptably dark brown or black.", "Storage & Economics"),
    ("Why do processing companies refuse potatoes stored in standard cold storages?", "Standard cold storages in Pakistan run at 2-4°C (which causes CIS). Processing companies require potatoes stored at higher temperatures (8-12°C) combined with sprout-inhibiting chemicals (CIPC).", "Storage & Economics"),
    ("What is CIPC (Chlorpropham) and why is it used?", "CIPC is a chemical sprout inhibitor fogged into potato storages kept at warmer temperatures (8-12°C). It stops the potatoes from sprouting while preventing the starch from turning into sugar.", "Storage & Economics"),
    ("What is 'weight loss' during cold storage?", "Potatoes are living organisms that respire and lose water. Poorly insulated cold storages with low humidity can cause the tubers to shrink and lose 5-10% of their weight over 6 months.", "Storage & Economics"),
    ("Why is Ammonia preferred over Freon in large Pakistani cold storages?", "Ammonia is highly energy-efficient for massive industrial cooling, has zero ozone depletion potential, and is significantly cheaper to refill than synthetic Freon refrigerants.", "Storage & Economics"),

    # --- Processing Quality & Specific Gravity ---
    ("What is Specific Gravity in potatoes?", "Specific gravity is a measurement of the dry matter (starch) content of the potato. It is measured by comparing the weight of the potato in air to its weight in water.", "Processing Quality"),
    ("Why do crisp/chip manufacturers demand high specific gravity?", "Potatoes with high specific gravity (more starch, less water) absorb less oil during frying, cook faster, and yield more chips per kilogram of raw potato, drastically improving factory profitability.", "Processing Quality"),
    ("Which potato varieties in Pakistan have the highest specific gravity for processing?", "Varieties like 'Lady Rosetta', 'Hermes', and 'Kuroda' are specifically bred for high dry matter and are the primary choices for the chips industry (e.g., Lays).", "Processing Quality"),
    ("What causes 'Hollow Heart' in potatoes?", "Hollow Heart is a physiological disorder where a star-shaped cavity forms in the center of a large tuber. It is caused by erratic, explosive growth spurts due to uneven irrigation or excess nitrogen.", "Processing Quality"),
    ("Why do processing factories reject tubers with 'Greening'?", "Greening occurs when tubers are exposed to sunlight in the field, causing them to produce Solanine, a toxic alkaloid that causes a bitter taste and is not destroyed by frying.", "Processing Quality")
]

filename = 'Pakistan_Potato_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality potato queries successfully!")
