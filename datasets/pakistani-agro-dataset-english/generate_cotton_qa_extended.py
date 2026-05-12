import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What type of soil is best for cotton cultivation in Pakistan?", "Cotton grows best in deep, well-drained, medium-heavy to sandy loam soils. Highly saline or waterlogged soils are unsuitable.", "Field Preparation"),
    ("Why is deep ploughing recommended for cotton?", "Cotton has a deep taproot system. Deep ploughing with a chisel plow breaks the hardpan, allowing roots to penetrate deeper for moisture and nutrients.", "Field Preparation"),
    ("What is the 'Rauni' irrigation in cotton farming?", "Rauni is the pre-sowing heavy irrigation applied to the field to ensure sufficient soil moisture (Watter condition) for seed germination.", "Field Preparation"),
    ("What is the recommended row-to-row spacing for cotton?", "The standard row-to-row spacing is 2.5 feet (75 cm) to allow proper aeration and sunlight.", "Field Preparation"),
    ("What should be the plant-to-plant distance for cotton?", "For normal sowing, a plant-to-plant distance of 9 to 12 inches is recommended. For early sowing, it can be increased to 15-18 inches.", "Field Preparation"),
    ("What is the bed-and-furrow method of planting cotton?", "Seeds are sown on raised beds, and irrigation is applied in furrows. This saves water, prevents seed rot, and keeps the plant stem dry.", "Field Preparation"),
    ("How many ploughings are typically required before sowing cotton?", "After Rauni, 2-3 ploughings followed by planking (Suhaga) are usually sufficient to prepare a fine seedbed.", "Field Preparation"),
    ("Why is laser land leveling beneficial for cotton?", "It ensures uniform water distribution across the field, saving up to 30% of irrigation water and ensuring uniform seed germination.", "Field Preparation"),
    ("Can cotton be grown on flat land?", "Yes, through drill sowing, but ridge/bed sowing is highly preferred in Pakistan to manage irrigation efficiently and protect against monsoon flooding.", "Field Preparation"),
    ("What is 'dry sowing' in cotton?", "Dry sowing involves planting seeds in dry soil and immediately applying irrigation. It is commonly practiced in heavy soils or when time is short.", "Field Preparation"),

    # --- Seed Selection & Treatment ---
    ("What is the recommended seed rate per acre for cotton?", "For acid-delinted (bur-free) seed, 6 to 8 kg per acre is recommended. For fuzzy (undelinted) seed, 10 to 12 kg is required.", "Seed Treatment"),
    ("What is acid delinting of cotton seed?", "It is the process of removing the fuzz from cotton seeds using commercial Sulphuric Acid. It improves germination and eliminates seed-borne diseases.", "Seed Treatment"),
    ("How is seed treatment performed for cotton?", "Seeds are treated with a systemic insecticide (like Imidacloprid or Thiamethoxam) and a fungicide before sowing.", "Seed Treatment"),
    ("Why is insecticide seed treatment critical for cotton?", "It protects the young cotton seedlings from early sucking pests like thrips, jassids, and whiteflies for the first 30-40 days.", "Seed Treatment"),
    ("What is Bt cotton?", "Bt (Bacillus thuringiensis) cotton is a genetically modified variety that produces a toxin lethal to bollworms (like pink and spotted bollworms).", "Seed Treatment"),
    ("Does Bt cotton protect against sucking pests?", "No, Bt technology only targets chewing pests (bollworms). Sucking pests like whiteflies and aphids still require chemical or biological control.", "Seed Treatment"),
    ("What is a 'refuge crop' in Bt cotton farming?", "Planting a non-Bt cotton variety on 5-10% of the field boundaries to prevent bollworms from developing resistance to the Bt toxin.", "Seed Treatment"),
    ("What is the optimal depth for sowing cotton seed?", "Seeds should be planted at a depth of 1.5 to 2 inches. Planting deeper can severely hinder emergence.", "Seed Treatment"),
    ("How to test cotton seed germination percentage at home?", "Place 100 seeds on a moist cloth or paper towel. If more than 75-80 seeds sprout within 5-7 days, the seed is viable.", "Seed Treatment"),
    ("What should be done if field germination is patchy?", "Gap filling (Chopa) should be done immediately, or within the first 10 days of sowing, by soaking seeds in water overnight before planting.", "Seed Treatment"),

    # --- Varieties of Pakistan ---
    ("What are some popular approved Bt cotton varieties in Pakistan?", "Popular varieties include IUB-2013, FH-142, MNH-886, CIM-602, Nayab-878, and BS-15.", "Varieties"),
    ("Are there any varieties resistant to Cotton Leaf Curl Virus (CLCuV)?", "While absolute immunity is rare, varieties like FH-142, IUB-2013, and certain CIM lines show high field tolerance to CLCuV.", "Varieties"),
    ("What is the importance of 'triple-gene' Bt cotton?", "Triple-gene varieties offer enhanced protection against a broader range of bollworms and delay the development of pest resistance.", "Varieties"),
    ("Should farmers save and reuse their own Bt cotton seed?", "It is not recommended, as subsequent generations lose their genetic purity, Bt toxin expression drops, and yields decrease significantly.", "Varieties"),
    ("Which variety is known for high heat tolerance?", "MNH-886 and Nayab-878 are well-regarded for their ability to tolerate high summer temperatures without excessive fruit shedding.", "Varieties"),

    # --- Provincial: Punjab ---
    ("Which province is the largest producer of cotton in Pakistan?", "Punjab produces roughly 65-70% of Pakistan's total cotton, primarily in the southern districts.", "Provincial: Punjab"),
    ("What is the core cotton belt in Punjab?", "The core cotton belt comprises South Punjab districts like Multan, Bahawalpur, Rahim Yar Khan, Vehari, and Lodhran.", "Provincial: Punjab"),
    ("What is the recommended sowing time for cotton in Punjab?", "The optimal sowing time in Punjab is from mid-April to the end of May.", "Provincial: Punjab"),
    ("What is 'early sowing' of cotton in Punjab?", "Some progressive farmers sow cotton in late February or March. This allows the crop to mature before peak pest attacks in late summer.", "Provincial: Punjab"),
    ("What is a major threat to the Punjab cotton crop during July-August?", "Heavy monsoon rains leading to waterlogging, combined with high humidity, trigger severe attacks of whitefly and Cotton Leaf Curl Virus.", "Provincial: Punjab"),
    ("Can cotton be intercropped with wheat in Punjab?", "Yes, 'relay cropping' is practiced where cotton is planted in standing wheat during February/March using specialized drills.", "Provincial: Punjab"),
    ("What is the 'Cotton Zone' restriction in Punjab?", "Historically, certain zones were restricted from growing crops like sugarcane or rice to prevent high humidity that favors cotton pests, though enforcement varies.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("When is cotton primarily sown in Sindh?", "Cotton in Sindh is sown earlier than Punjab, typically from March to mid-April, due to the earlier onset of summer.", "Provincial: Sindh"),
    ("Which districts are the major cotton producers in Sindh?", "Sanghar, Nawabshah (Shaheed Benazirabad), Mirpurkhas, Khairpur, and Sukkur are the leading districts.", "Provincial: Sindh"),
    ("What climatic advantage does Sindh have for cotton?", "The hot, dry winds help keep the incidence of Cotton Leaf Curl Virus (CLCuV) much lower compared to Punjab.", "Provincial: Sindh"),
    ("Which cotton varieties perform well in Sindh?", "Varieties developed by local institutes, such as Sindh-1, Hari Dost, and Sadori, are well-adapted to the local climate.", "Provincial: Sindh"),
    ("What is the primary challenge for cotton farmers in lower Sindh?", "Shortage of irrigation water during the critical early sowing months (March-April) is a major constraint.", "Provincial: Sindh"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("Is cotton grown in Khyber Pakhtunkhwa?", "Yes, but on a much smaller scale compared to Punjab and Sindh.", "Provincial: KPK"),
    ("Which area of KPK is known for cotton cultivation?", "Dera Ismail Khan (D.I. Khan) is the primary cotton-growing district in KPK due to its plain topography and warmer climate.", "Provincial: KPK"),
    ("What is the sowing time for cotton in KPK?", "Sowing is generally done in May when the temperature becomes optimal for germination.", "Provincial: KPK"),
    ("What is a major advantage of growing cotton in D.I. Khan?", "The area has a very low incidence of Cotton Leaf Curl Virus (CLCuV) and certain pests, resulting in good quality lint.", "Provincial: KPK"),

    # --- Provincial: Balochistan ---
    ("Where is cotton cultivated in Balochistan?", "Cotton is mainly cultivated in the plain areas adjacent to Sindh, such as Nasirabad, Jaffarabad, and Lasbela.", "Provincial: Balochistan"),
    ("What is the unique feature of Balochistan's cotton?", "Balochistan produces highly organic, clean cotton with excellent staple length due to minimal pest pressure and low pesticide use.", "Provincial: Balochistan"),
    ("What is the sowing time in Balochistan?", "Sowing usually takes place from April to May.", "Provincial: Balochistan"),
    ("Why is Balochistan considered a potential future hub for cotton?", "Its arid climate naturally suppresses viral diseases and bollworms, making it ideal for organic and high-quality export cotton.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the general NPK fertilizer recommendation for cotton?", "Apply 1.5 to 2 bags of DAP, 3 to 4 bags of Urea, and 1 bag of SOP (Sulphate of Potash) per acre.", "Fertilizer Management"),
    ("When should Phosphorus (DAP) be applied to cotton?", "The entire dose of DAP must be applied at the time of final field preparation before sowing.", "Fertilizer Management"),
    ("How should Nitrogen (Urea) be applied to cotton?", "Urea should be applied in 3 to 4 equal splits: at sowing, at first flower bud (square) formation, at peak flowering, and at boll formation.", "Fertilizer Management"),
    ("Why is Potash (SOP) important for cotton?", "Potash improves boll size, staple length, fiber strength, and the plant's resistance to drought and diseases.", "Fertilizer Management"),
    ("What causes fruit (square/boll) shedding in cotton?", "Shedding is primarily caused by heat stress, water stress, or a deficiency in Nitrogen or Boron.", "Fertilizer Management"),
    ("How and when to apply Boron to the cotton crop?", "Boron prevents boll shedding. Spray 300g of Boric Acid per acre at the onset of flowering, or apply 1-2 kg to the soil.", "Fertilizer Management"),
    ("What is the symptom of Zinc deficiency in cotton?", "Leaves become small, thick, and cup-shaped, and internodes shorten (rosetting). Apply Zinc Sulphate during early vegetative growth.", "Fertilizer Management"),
    ("What causes reddening of cotton leaves?", "Reddening late in the season is often caused by Magnesium or Nitrogen deficiency, combined with low night temperatures.", "Fertilizer Management"),
    ("Can foliar feeding of Urea benefit cotton?", "Yes, a 2% Urea spray during peak boll formation helps meet the high nitrogen demand and prevents premature leaf aging.", "Fertilizer Management"),
    ("Why should late application of Urea be avoided?", "Applying Urea late in the season delays maturity, promotes excessive vegetative growth, and heavily attracts sucking pests.", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("How many irrigations are generally required for a cotton crop?", "Cotton typically requires 6 to 8 irrigations depending on rainfall and soil type.", "Irrigation & Weeds"),
    ("When should the first irrigation be given after sowing?", "For flat sowing, the first irrigation is given 30-40 days after sowing. For bed planting, it is given much earlier, around 3-5 days.", "Irrigation & Weeds"),
    ("What is the critical stage for irrigation in cotton?", "The flowering and boll development stages (July-August) are highly critical; water stress here causes massive boll shedding.", "Irrigation & Weeds"),
    ("How to irrigate cotton during the monsoon season?", "Irrigation should be delayed if rain is expected. Proper drainage must be ensured as standing water for 24-48 hours causes root rot and wilting.", "Irrigation & Weeds"),
    ("When should irrigation be stopped before picking?", "Stop irrigation 15 to 20 days before the first picking to encourage boll opening and defoliation.", "Irrigation & Weeds"),
    ("What are the major weeds in the cotton field?", "Common weeds include Itsit (Trianthema), Deela (Cyperus rotundus), and Khabbal grass (Cynodon dactylon).", "Irrigation & Weeds"),
    ("Which pre-emergence herbicides are used in cotton?", "Pendimethalin or S-Metolachlor are sprayed on moist soil within 24 hours of sowing to prevent weed germination.", "Irrigation & Weeds"),
    ("Can Glyphosate be used in standing cotton?", "Glyphosate is a non-selective herbicide. It can only be used with a protective shield over the nozzle to prevent spray drift onto the cotton plants.", "Irrigation & Weeds"),
    ("Why is manual hoeing (Godi) recommended in early stages?", "Hoeing breaks the hard soil crust, removes weeds, and aerates the root zone, significantly boosting plant vigor.", "Irrigation & Weeds"),
    ("What is 'cotton thinning'?", "Thinning is the removal of excess, weak seedlings 20-25 days after sowing to maintain the optimal plant-to-plant distance.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("What is the most dangerous sucking pest of cotton in Pakistan?", "The Whitefly is the most dangerous pest. It sucks sap, reduces yield, and vectors the deadly Cotton Leaf Curl Virus.", "Pest Management"),
    ("How to control a severe whitefly attack?", "Rotate chemistries. Spray insect growth regulators (like Pyriproxyfen) to kill nymphs, and adulticides (like Flonicamid or Diafenthiuron) for adults.", "Pest Management"),
    ("What are the symptoms of Jassid attack on cotton?", "Jassids suck sap from the underside of leaves, injecting a toxin that causes the leaf edges to turn yellow, cup downward, and eventually turn red (hopper burn).", "Pest Management"),
    ("How to control Jassid in cotton?", "Spray systemic insecticides like Imidacloprid, Nitenpyram, or Dinotefuran.", "Pest Management"),
    ("What are the signs of a Thrips attack?", "Thrips scrape the leaf surface and suck the sap. The leaves develop a silvery, scarred appearance and cup upwards.", "Pest Management"),
    ("How to manage Thrips in the early stage?", "Seed treatment is the first defense. Later, spray Spinetoram, Chlorfenapyr, or Fipronil if the population exceeds the economic threshold.", "Pest Management"),
    ("What is the Pink Bollworm and why is it so damaging?", "The pink bollworm larva enters the cotton boll, eats the seeds, and destroys the lint. Because it feeds inside the boll, chemical sprays are often ineffective.", "Pest Management"),
    ("How to manage the Pink Bollworm effectively?", "Use PB ropes (mating disruption), install pheromone traps for monitoring, avoid late sowing, and graze/burn crop residues after harvest.", "Pest Management"),
    ("What are PB ropes?", "Pink Bollworm (PB) Ropes are wires coated with female sex pheromones. Tied to plants, they confuse the males, preventing mating.", "Pest Management"),
    ("What is the Armyworm and how to control it?", "Armyworms are leaf-eating caterpillars that feed voraciously in groups. Spray Emamectin Benzoate or Lufenuron in the evening.", "Pest Management"),
    ("How do aphids damage the cotton crop?", "Aphids cluster on young shoots, sucking sap and excreting sticky 'honeydew', on which black sooty mold grows, blocking photosynthesis.", "Pest Management"),
    ("What is the role of beneficial insects (farmer friends) in cotton?", "Predators like Ladybird beetles, Chrysoperla (Green lacewing), and Spiders naturally control aphids, whiteflies, and bollworm eggs.", "Pest Management"),
    ("Why should early chemical spraying be avoided?", "Spraying broad-spectrum insecticides in the first 40 days kills beneficial insects, leading to massive pest resurgences later in the season.", "Pest Management"),
    ("What is the Economic Threshold Level (ETL)?", "ETL is the pest population level at which spraying becomes economically justified. E.g., for whitefly, it is 5 adults/nymphs per leaf.", "Pest Management"),
    ("How to control mealybugs in cotton?", "Mealybugs form white, waxy clusters on stems. Remove and burn heavily infested plants. Spray Profenofos mixed with a detergent/surfactant.", "Pest Management"),

    # --- Disease Management ---
    ("What is Cotton Leaf Curl Virus (CLCuV)?", "CLCuV is a viral disease that causes upward or downward curling of leaves, thickened veins, and leaf-like outgrowths (enations) on the underside.", "Disease Management"),
    ("How is CLCuV transmitted?", "The virus is transmitted exclusively by the whitefly vector.", "Disease Management"),
    ("Is there a chemical cure for CLCuV?", "No. The only management strategy is to grow tolerant varieties, eradicate alternative weed hosts, and aggressively control the whitefly population.", "Disease Management"),
    ("What causes Cotton Boll Rot?", "Boll rot is caused by fungi and bacteria thriving in high humidity, heavy rains, or dense crop canopies where sunlight cannot reach lower bolls.", "Disease Management"),
    ("How to prevent Boll Rot?", "Avoid excessive nitrogen (which makes the canopy too dense), control bollworms (whose holes allow fungi to enter), and ensure proper plant spacing.", "Disease Management"),
    ("What is Fusarium Wilt in cotton?", "It is a soil-borne fungal disease that enters through the roots, blocking water transport and causing the plant to wilt and die. Roots show brown discoloration.", "Disease Management"),
    ("How to manage Cotton Wilt?", "Use disease-free seed, practice crop rotation, ensure proper drainage, and apply Trichoderma (a beneficial fungus) to the soil.", "Disease Management"),
    ("What is bacterial blight (Angular Leaf Spot)?", "It causes water-soaked, angular dark brown spots on leaves. It is managed by seed delinting and spraying copper-based fungicides.", "Disease Management"),
    ("What causes the sudden drying/parawilt of cotton plants after irrigation?", "This physiological disorder (parawilt) occurs when a crop that faced a long drought is suddenly irrigated on a hot day. The roots suffocate and the plant wilts.", "Disease Management"),

    # --- Harvesting & Storage ---
    ("When does cotton picking usually begin in Pakistan?", "The first picking usually starts in August or September, depending on the sowing time, when 50-60% of the bolls have fully opened.", "Harvesting & Storage"),
    ("What is the best time of day to pick cotton?", "Picking should start after 10:00 AM once the morning dew has dried. Picking wet cotton reduces its grade and causes rotting during storage.", "Harvesting & Storage"),
    ("Why is clean cotton picking important?", "Lint mixed with dried leaves, sticks, or trash receives a lower grade at the ginning factory, resulting in poor prices for the farmer.", "Harvesting & Storage"),
    ("What type of bags should be used for picking and storing cotton?", "Only use pure cotton cloth bags. NEVER use polypropylene (plastic) fertilizer bags, as plastic fibers ruin the spinning machinery at textile mills.", "Harvesting & Storage"),
    ("How many pickings are normally done?", "Usually, 3 to 4 pickings are done at intervals of 15 to 20 days as new bolls continue to open.", "Harvesting & Storage"),
    ("How should harvested cotton be stored on the farm?", "It should be stored in a dry, covered, well-ventilated area on raised wooden planks to prevent moisture absorption from the floor.", "Harvesting & Storage"),
    ("What should be done with the cotton field after the final picking?", "The stems (sticks) should be cut, and the stubble must be uprooted or shredded using a rotavator to kill overwintering pink bollworm pupae.", "Harvesting & Storage"),

    # --- FAQs: Economics, Yield, Marketing ---
    ("What is the average yield of cotton per acre in Pakistan?", "The national average is around 20-25 maunds (800-1000 kg) per acre, though progressive farmers regularly achieve 40-50 maunds.", "FAQs"),
    ("What causes the decline in Pakistan's total cotton production in recent years?", "Climate change (unseasonal rains, extreme heat), aggressive whitefly/CLCuV attacks, and farmers shifting to sugarcane and maize due to better profitability.", "FAQs"),
    ("How is the price of Phutti (seed cotton) determined in the local market?", "The price is determined by the global lint market, the staple length of the variety, and the cleanliness (trash percentage) of the harvest.", "FAQs"),
    ("What is a 'maund' in the context of Pakistani agriculture?", "A maund is a traditional unit of weight equal to exactly 40 kilograms.", "FAQs"),
    ("What is Cotton Ginning?", "Ginning is the mechanical process of separating the cotton fibers (lint) from the cotton seeds (Banola).", "FAQs"),
    ("What is the economic value of cotton seeds (Banola)?", "Cotton seeds are highly valuable. They are crushed to extract edible oil, and the remaining seed cake (Khal) is an excellent protein-rich feed for livestock.", "FAQs"),
    ("What is the 'support price' for cotton in Pakistan?", "The government occasionally sets an intervention/support price to protect farmers from market crashes, ensuring they recover their cost of production.", "FAQs"),
    ("How does crop rotation improve cotton yields?", "Rotating cotton with wheat or legumes breaks the pest lifecycle (especially pink bollworm) and restores soil fertility.", "FAQs"),
    ("What is staple length, and why does it matter?", "Staple length is the length of the individual cotton fiber. Longer staples fetch premium prices because they produce stronger, finer yarn in textile mills.", "FAQs"),
    # --- Advanced Cotton Agronomy & Pathology ---
    ("What is Mepiquat Chloride (Pix) and why is it used?", "It is a plant growth regulator sprayed on cotton to restrict excessive vegetative (leafy) growth, directing the plant's energy into boll formation and preventing the canopy from becoming too dense.", "Advanced Agronomy"),
    ("Why is canopy management critical in Bt cotton?", "A dense, overgrown canopy blocks sunlight to the lower bolls, causing boll rot, and creates a humid microclimate that severely exacerbates whitefly and mealybug outbreaks.", "Advanced Agronomy"),
    ("Has the Pink Bollworm developed resistance to Bt Cotton in Pakistan?", "Yes, continuous planting of single-gene Bt cotton without 'refuge crops' has allowed the Pink Bollworm to develop significant resistance, making supplementary pheromone/chemical control mandatory.", "Pest Management"),
    ("What is the 'Refuge Crop' strategy?", "Planting 5-10% of the field with non-Bt cotton varieties. This allows susceptible bollworms to survive and mate with any resistant bollworms, diluting the resistance gene in the pest population.", "Pest Management"),
    ("How do PB Ropes (Mating Disruption) work exactly?", "PB Ropes release synthetic female sex pheromones continuously. This saturates the air, confusing the male pink bollworms so they cannot locate females to mate, crashing the next generation's population.", "Pest Management"),
    ("What are the alternate hosts for Cotton Leaf Curl Virus (CLCuV)?", "The virus and its whitefly vector survive the winter on alternate hosts like Okra (Bhindi), Cotton/China Rose, and weeds like Itsit. Eradicating these around cotton fields is vital.", "Disease Management"),
    ("What is 'Ginning Out-Turn' (GOT) in cotton?", "GOT is the percentage of pure lint obtained from seed cotton (Phutti). Pakistani varieties typically have a GOT of 33% to 38%, meaning 100 kg of Phutti yields 33-38 kg of lint and the rest is seed (Banola) and trash.", "Economics & Marketing"),
    ("Why does early picking of wet cotton lower its market price?", "Picking cotton early in the morning when it is wet with dew causes the fibers to stain, encourages fungal rot during storage, and makes ginning very difficult, resulting in heavy price deductions.", "Harvest & Post-Harvest"),
    ("What is 'Stickiness' in cotton lint?", "Stickiness is caused by the sugary honeydew excreted by severe infestations of Whiteflies or Aphids late in the season. It severely jams the spinning machinery in textile mills, ruining the lint's value.", "Harvest & Post-Harvest")
]

filename = 'Pakistan_Cotton_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality cotton queries successfully!")
