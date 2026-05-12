import csv

qa_data = [
    # --- Orchard Establishment & Planting ---
    ("What is the most suitable soil for planting a mango orchard in Pakistan?", "Mangoes thrive in deep, well-drained, fertile loamy to sandy-loam soils. Highly alkaline, saline, or waterlogged soils stunt growth and cause nutrient deficiencies.", "Orchard Establishment"),
    ("What is the ideal time for planting mango saplings?", "The best times for planting are during the spring (February-March) and the monsoon season (August-September) when the weather is mild and humid.", "Orchard Establishment"),
    ("What is the traditional spacing for planting a mango orchard?", "Traditional spacing is usually 30x30 feet or 35x35 feet, accommodating about 35 to 48 plants per acre.", "Orchard Establishment"),
    ("What is High-Density Planting (HDP) in mangoes?", "HDP involves planting trees closer together (e.g., 15x15 feet or 10x15 feet) and maintaining a small canopy through rigorous pruning. It drastically increases early yields per acre.", "Orchard Establishment"),
    ("How should a pit be prepared before planting a mango sapling?", "Dig a 3x3x3 feet pit, expose it to the sun for a week, and fill it with a mixture of topsoil, well-rotted Farm Yard Manure (FYM), and a soil insecticide to prevent termites.", "Orchard Establishment"),
    ("Why is windbreak planting important around a mango orchard?", "Strong hot winds (Loo) in summer and cold drafts in winter can damage young plants and cause severe fruit drop. Trees like Eucalyptus or Shisham are planted on boundaries to block wind.", "Orchard Establishment"),

    # --- Propagation & Grafting ---
    ("Why are commercial mangoes not grown from seeds?", "Mangoes grown from seeds do not retain the characteristics of the parent tree (they are cross-pollinated) and take 8-10 years to bear fruit. Vegetative propagation ensures true-to-type plants.", "Propagation"),
    ("What is the most common grafting method used for mangoes in Pakistan?", "Veneer grafting and T-budding are the most commercially successful methods used in local nurseries.", "Propagation"),
    ("What is a 'rootstock' in mango grafting?", "The rootstock is the seedling plant (usually grown from a vigorous, disease-resistant 'Desi' mango seed) onto which the desired commercial variety (scion) is grafted.", "Propagation"),
    ("At what height should grafting ideally be done on the rootstock?", "Grafting is usually done at a height of 9 to 12 inches from the soil surface to ensure a strong trunk and prevent soil-borne diseases from reaching the graft union.", "Propagation"),

    # --- Varieties of Pakistan ---
    ("What is the most famous mango variety of Sindh?", "The 'Sindhri' mango is the pride of Sindh. It is large, yellow, oval-shaped, highly aromatic, and excellent for commercial export.", "Varieties"),
    ("What are the most famous varieties of Punjab?", "Punjab is famous for 'Chaunsa' (White, Samar Bahisht, and Black), 'Anwar Ratol' (known for intense aroma/sweetness), 'Langra', and 'Dussehri'.", "Varieties"),
    ("What is the 'Chaunsa' mango?", "Chaunsa is globally recognized as one of the sweetest mangoes. It has soft, almost fiberless flesh and a distinct, rich aroma. It matures in mid-to-late summer.", "Varieties"),
    ("Which mango variety comes earliest in the market?", "The 'Saroli' and 'Dussehri' are early-season varieties, hitting the market in late May and early June.", "Varieties"),
    ("Which mango variety is available latest in the season?", "The 'Fajri' and 'Black Chaunsa' (Kala Chaunsa) are late-season varieties available in late August and September.", "Varieties"),

    # --- Provincial: Sindh ---
    ("Why do Sindh mangoes arrive in the market earlier than Punjab mangoes?", "The warmer coastal and southern climate of Sindh triggers early flowering and fruit maturation, bringing Sindhri and Dussehri to market by late May.", "Provincial: Sindh"),
    ("What are the core mango-producing districts in Sindh?", "Mirpurkhas, Hyderabad, Tando Allahyar, Matiari, and Sanghar are the leading districts for mango production in Sindh.", "Provincial: Sindh"),
    ("What specific climatic advantage does Sindh have for mangoes?", "The hot and dry pre-monsoon winds enhance the sweetness and uniform ripening of the Sindhri variety.", "Provincial: Sindh"),

    # --- Provincial: Punjab ---
    ("What is the 'Mango Belt' of Punjab?", "The southern region of Punjab, specifically Multan, Rahim Yar Khan, Muzaffargarh, Bahawalpur, and Khanewal, is the world-renowned mango belt.", "Provincial: Punjab"),
    ("What makes Multan historically significant for mangoes?", "Multan has the perfect hot, arid summer climate and fertile alluvial soils that contribute to the unique flavor profile of the Chaunsa and Anwar Ratol varieties.", "Provincial: Punjab"),
    ("What is a major threat to the Punjab mango crop during late summer?", "Heavy, unexpected monsoon rains accompanied by windstorms (Aandhi) can cause massive premature fruit drop and trigger fungal diseases like Anthracnose.", "Provincial: Punjab"),

    # --- Provincial: KPK & Balochistan ---
    ("Are mangoes grown in Khyber Pakhtunkhwa (KPK)?", "Mango cultivation in KPK is very limited, mostly confined to the warmer southern district of D.I. Khan, producing late-maturing local varieties.", "Provincial: KPK & Balochistan"),
    ("Why is mango farming virtually non-existent in Balochistan?", "Mango trees cannot survive the severe winter frost and snow in northern Balochistan, nor the extreme water scarcity in the southern parts.", "Provincial: KPK & Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the general fertilizer schedule for a mature mango tree?", "Apply FYM in December. Apply Phosphorus (DAP) and Potash (SOP) in January. Apply Nitrogen (Urea) in two splits: before flowering (Feb) and after fruit set (April).", "Fertilizer Management"),
    ("Why is Zinc important for mango trees?", "Zinc prevents 'Little Leaf' disease and Rosetting, ensuring healthy vegetative flushes. It is usually sprayed as Zinc Sulphate.", "Fertilizer Management"),
    ("What causes fruit cracking in mangoes?", "Fruit cracking is primarily caused by Boron deficiency and erratic moisture fluctuations in the soil during fruit development.", "Fertilizer Management"),
    ("How to prevent fruit cracking?", "Apply Borax to the soil in winter or spray Boric acid during the pea-sized fruit stage, and maintain consistent soil moisture.", "Fertilizer Management"),
    ("What causes yellowing of mango leaves (chlorosis)?", "Chlorosis is often caused by Iron or Nitrogen deficiency, especially in highly alkaline (calcareous) soils of southern Punjab. Foliar sprays of Ferrous Sulphate are effective.", "Fertilizer Management"),

    # --- Flowering, Fruit Set & Drop ---
    ("What causes lack of flowering in mature mango trees?", "It can be caused by excessive vegetative growth (due to over-application of Nitrogen), lack of pruning, dense canopy shading, or a heavy crop in the previous year.", "Flowering & Fruiting"),
    ("What is 'Alternate Bearing' in mangoes?", "It is a natural tendency of many mango varieties (like Dussehri and Langra) to produce a heavy crop one year (On-year) and a very poor crop the next year (Off-year).", "Flowering & Fruiting"),
    ("How to manage Alternate Bearing?", "Use Paclobutrazol (a growth retardant) as a soil drench in September/October, prune trees annually, and apply balanced fertilizers to encourage regular flowering.", "Flowering & Fruiting"),
    ("Why do mango flowers drop without setting fruit?", "Flower drop is caused by high temperatures, fog, heavy rains washing away pollen, fungal infections (Powdery Mildew), or Mango Hopper attacks during full bloom.", "Flowering & Fruiting"),
    ("Why does premature fruit drop occur?", "It occurs due to nutrient deficiencies, moisture stress, strong winds, or hormonal imbalances. Natural drop (June drop) is normal as the tree sheds excess fruit it cannot support.", "Flowering & Fruiting"),
    ("How to control excessive premature fruit drop?", "Apply regular, light irrigations to avoid moisture stress, ensure Boron/Zinc application, and spray synthetic growth hormones like NAA (Naphthalene Acetic Acid) at the pea stage.", "Flowering & Fruiting"),

    # --- Pest Management ---
    ("What is the Mango Hopper and how does it damage the crop?", "The Mango Hopper is the most destructive pest. It sucks sap from tender panicles (flowers) and young leaves, causing the flowers to wither and drop completely.", "Pest Management"),
    ("How to control the Mango Hopper?", "Spray Imidacloprid, Thiamethoxam, or Clothianidin just before the flowers open, and again at the pea-sized fruit stage. Never spray during full bloom to protect pollinating bees.", "Pest Management"),
    ("What is the Mango Mealy Bug and how to manage it?", "Mealy bugs are white, cottony insects that crawl up the trunk in late winter. Control them by wrapping a sticky band or slippery plastic sheet around the tree trunk in December.", "Pest Management"),
    ("What is the Fruit Fly and why is it dangerous?", "The female fruit fly punctures the ripening mango skin and lays eggs. Maggots hatch and feed on the pulp, causing the fruit to rot from the inside, devastating export potential.", "Pest Management"),
    ("How to control the Mango Fruit Fly?", "Install Methyl Eugenol pheromone traps in the orchard, pick up and bury all fallen/rotting fruits, and apply bait sprays.", "Pest Management"),
    ("How does the Stem Borer attack mango trees?", "The large beetle lays eggs under the bark. The hatching grubs bore deep tunnels into the main trunk, cutting off sap supply and potentially killing massive branches.", "Pest Management"),
    ("How to treat a Stem Borer infestation?", "Find the hole, clean out the frass (sawdust), insert a cotton swab soaked in Dichlorvos or Kerosene, and seal the hole tightly with mud to suffocate the grub.", "Pest Management"),
    ("What is the Mango Pulp Weevil?", "A pest where the adult lays eggs on the young fruit, and the larva feeds and pupates entirely inside the flesh or seed, making detection very difficult until the fruit is cut open.", "Pest Management"),
    ("What is the Mango Midges pest?", "Gall midges attack the leaves, creating small blister-like galls, and also attack the inflorescence, causing severe flower drop. Managed by pruning and systemic insecticides.", "Pest Management"),

    # --- Disease Management ---
    ("What is Powdery Mildew in mango?", "A fungal disease that covers the flowers (panicles) and young leaves with a white powdery dust, leading to massive flower drop and no fruit set.", "Disease Management"),
    ("How to control Powdery Mildew?", "Spray Sulphur-based fungicides, Hexaconazole, or Difenoconazole right before flowering and during the early fruit set stage.", "Disease Management"),
    ("What is Anthracnose?", "A fungal disease causing black, sunken spots on leaves, flowers, and ripening fruits. It thrives in high humidity and rain, causing 'tear-stain' marks on the fruit.", "Disease Management"),
    ("How to manage Anthracnose?", "Prune the canopy to allow sunlight and airflow. Spray Copper Oxychloride or Mancozeb. For harvested fruits, hot water treatment provides excellent control.", "Disease Management"),
    ("What is Mango Malformation Disease (MMD)?", "It is a highly destructive, poorly understood fungal disease where flowers bunch together in a dense, vegetative mass ('Witches broom') and completely fail to produce fruit.", "Disease Management"),
    ("How to control Mango Malformation?", "There is no chemical cure. The only control is to physically cut the malformed panicles along with 1 foot of healthy branch below it and burn them immediately.", "Disease Management"),
    ("What causes Sooty Mould on mango leaves?", "Sooty mould is a black, crusty fungus that grows on the sweet, sticky 'honeydew' excreted by pests like Mango Hoppers and Mealy Bugs.", "Disease Management"),
    ("How to control Sooty Mould?", "Since it grows on insect excretions, controlling the underlying pest (Hoppers/Mealy Bugs) prevents it. A strong spray of water mixed with a mild starch solution helps peel it off.", "Disease Management"),
    ("What is 'Spongy Tissue' in mangoes?", "It is a physiological disorder (not a disease) common in Sindhri, where a patch of flesh inside the ripe mango remains unripe, white, and corky.", "Disease Management"),
    ("What causes Spongy Tissue?", "It is caused by excessive heat convecting from the soil surface into the hanging fruit. Maintaining a green ground cover or mulching under the tree reduces its incidence.", "Disease Management"),

    # --- Irrigation & Canopy Management ---
    ("How often should a mature mango orchard be irrigated?", "Irrigate every 10-15 days during the hot summer (fruit development stage). Stop irrigation entirely in November-December to induce stress, which promotes flowering.", "Irrigation & Canopy Management"),
    ("Why is canopy pruning necessary for mango trees?", "Pruning removes dead, diseased, and overlapping branches. It opens up the center of the tree to sunlight and aeration, which drastically reduces fungal diseases and improves fruit color.", "Irrigation & Canopy Management"),
    ("When is the best time to prune a mango tree in Pakistan?", "The best time is immediately after the fruit harvest (August-September).", "Irrigation & Canopy Management"),

    # --- Harvesting, Post-Harvest & Export ---
    ("How to determine if a mango is ready for harvest?", "The fruit is mature when the shoulders broaden, the color slightly changes, the pedicel (stalk) dries, and the specific gravity reaches a point where the fruit sinks in water.", "Harvest & Post-Harvest"),
    ("How should mangoes be harvested?", "Mangoes must be hand-picked using a net attached to a long pole with a blade. They should never be allowed to fall to the ground, as bruised fruits rot quickly.", "Harvest & Post-Harvest"),
    ("What is the significance of the 'sap' or 'latex' during harvesting?", "When the stem is snapped, highly acidic sap squirts out. If it touches the mango skin, it causes ugly black sapburns. Mangoes must be de-sapped immediately.", "Harvest & Post-Harvest"),
    ("What is Hot Water Treatment (HWT)?", "HWT involves dipping harvested mangoes in water heated to 48°C for 60 minutes. It kills fruit fly eggs inside the fruit and eliminates surface fungal spores.", "Harvest & Post-Harvest"),
    ("Why is HWT critical for Pakistan's mango industry?", "HWT is a mandatory quarantine requirement for exporting mangoes to lucrative markets like the European Union, UK, and Iran to prevent the spread of the fruit fly.", "Harvest & Post-Harvest"),
    ("How long can mangoes be stored in cold storage?", "Mature green mangoes can be stored at 12-13°C for up to 3 to 4 weeks. Storing below 10°C causes chilling injury (skin blackening and poor ripening).", "Harvest & Post-Harvest"),
    ("How are mangoes artificially ripened safely?", "They are exposed to Ethylene gas in specialized ripening chambers. The old practice of using Calcium Carbide (Masala) is toxic, banned, and hazardous to human health.", "Harvest & Post-Harvest"),

    # --- FAQs ---
    ("What is the average yield of a mature mango orchard in Pakistan?", "A well-managed orchard yields between 8 to 12 tons per acre, though the national average is lower due to poor management.", "FAQs"),
    ("Why is 'Anwar Ratol' highly priced and often in short supply?", "It is a premium, highly aromatic, small-sized mango with very short shelf life and limited cultivation area, creating high demand and premium pricing.", "FAQs"),
    ("What is 'Mango Dieback'?", "A disease causing the branches to dry and die from the tip downwards, often accompanied by gum oozing. It is managed by pruning below the infected part and applying Copper fungicides.", "FAQs"),
    ("Are mango trees susceptible to frost?", "Yes, young mango saplings under 3 years old are highly sensitive to winter frost. They must be covered with plastic sheets or thatch (Sarkanda) during December and January.", "FAQs"),
    ("Can multiple mango varieties be grafted onto a single tree?", "Yes, this technique is called 'top-working'. A farmer can graft branches of Chaunsa, Sindhri, and Langra onto the same mature rootstock tree.", "FAQs"),
    # --- Advanced Mango Horticulture & Export ---
    ("What is the Alternate Bearing phenomenon in mangoes?", "It is the tendency of mango trees to produce a heavy crop one year (on-year) and a very light or no crop the next year (off-year), heavily driven by genetics and environmental stress.", "Advanced Horticulture"),
    ("How is Paclobutrazol (Cultar) used to manage alternate bearing?", "Paclobutrazol is a growth retardant applied as a soil drench around the tree trunk in late summer. It restricts vegetative growth and strongly induces early and uniform flowering for the next season.", "Advanced Horticulture"),
    ("What is Mango Sudden Death Syndrome (MSDS)?", "MSDS is a devastating fungal disease (primarily Ceratocystis fimbriata) spread by the bark beetle. It causes rapid wilting and complete death of mature trees within weeks, with dark gummy sap oozing from the bark.", "Disease Management"),
    ("How to manage Mango Malformation disease?", "Caused by the Fusarium fungus, it turns flower panicles into thick, sterile, leafy masses. The only control is to rigorously prune out and burn the malformed shoots 1.5 feet below the affected area.", "Disease Management"),
    ("What is the 'Spongy Tissue' disorder in Sindhri and Chaunsa?", "It is a physiological disorder where a patch of flesh inside the ripe fruit remains hard, pale, and acidic while the rest ripens. It is caused by convective heat from the soil during maturation.", "Physiological Disorders"),
    ("What are the exact parameters for Hot Water Treatment (HWT) for mango export?", "To eradicate fruit fly eggs/larvae and meet strict export quarantine standards, mangoes must be submerged in water at exactly 48°C for 60 minutes.", "Export & Post-Harvest"),
    ("What is High-Density Plantation (HDP) in mangoes?", "Instead of traditional wide spacing (40x40 ft), HDP involves planting trees very closely (e.g., 15x15 ft) and using aggressive canopy pruning to keep trees small, significantly increasing yield per acre.", "Advanced Horticulture"),
    ("What is Veneer Grafting and when is it done?", "Veneer grafting is a highly successful vegetative propagation method where a scion is attached to the side of a rootstock. It is typically done in July-August during high humidity.", "Advanced Horticulture"),
    ("Why must mangoes be harvested leaving a 1 cm pedicel (stem)?", "Harvesting with a short stem prevents the highly acidic 'sap burn' (which ruins the skin) from oozing directly onto the fruit, preventing secondary fungal rots during transport.", "Export & Post-Harvest")
]

filename = 'Pakistan_Mango_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality mango queries successfully!")
