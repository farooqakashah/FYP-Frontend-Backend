import csv

qa_data = [
    # Sowing & Field Preparation (15)
    ("What is the optimal sowing time for wheat in Punjab and Sindh?", "The optimal sowing time is from November 1 to November 20. Sowing during this window ensures maximum yield.", "Sowing & Field Preparation"),
    ("How does late sowing affect wheat yield?", "Delaying sowing beyond November reduces yield by approximately 15-20 kg per acre per day due to reduced tillering and grain size.", "Sowing & Field Preparation"),
    ("What is the optimal sowing time for wheat in KP and Balochistan?", "In northern and hilly areas, the ideal sowing window is earlier, typically from mid-October to early November.", "Sowing & Field Preparation"),
    ("What is the recommended seed rate for timely sown wheat per acre?", "For timely sowing (early to mid-November), a seed rate of 40 to 50 kg per acre is recommended.", "Sowing & Field Preparation"),
    ("What is the seed rate for late-sown wheat (December)?", "Increase the seed rate to 50 to 60 kg per acre to compensate for the reduced tillering caused by lower temperatures.", "Sowing & Field Preparation"),
    ("How many ploughings are needed to prepare the field for wheat?", "Usually, 2-3 ploughings followed by 1-2 planking (Suhaga) are sufficient to create a fine, well-pulverized seedbed.", "Sowing & Field Preparation"),
    ("What is 'Rauni' in wheat cultivation?", "Rauni is the pre-sowing irrigation applied to the field to ensure adequate moisture for seed germination.", "Sowing & Field Preparation"),
    ("At what soil moisture level should wheat be sown?", "Wheat should be sown at the 'Watter' condition, which is when the soil has workable moisture but is not too wet.", "Sowing & Field Preparation"),
    ("What is the recommended sowing method for wheat?", "Drill sowing (using a Rabi drill) is highly recommended over broadcasting, as it places seeds at uniform depth and spacing.", "Sowing & Field Preparation"),
    ("What is the ideal row-to-row distance for wheat?", "The recommended row-to-row distance is 9 inches (22.5 cm) for standard drill sowing.", "Sowing & Field Preparation"),
    ("Is deep ploughing necessary for wheat?", "Wheat has a relatively shallow fibrous root system, so deep ploughing is usually not required unless there is a hardpan in the soil.", "Sowing & Field Preparation"),
    ("How deep should wheat seeds be planted?", "Seeds should be planted at a depth of 2 to 2.5 inches. Planting deeper can severely delay or prevent germination.", "Sowing & Field Preparation"),
    ("Can wheat be sown on ridges/beds?", "Yes, bed planting (sowing on raised beds) is gaining popularity. It saves up to 30-40% water and prevents lodging.", "Sowing & Field Preparation"),
    ("What is the zero-tillage method for wheat?", "Zero-tillage involves sowing wheat directly into rice stubble without ploughing, using a specialized zero-till drill. It saves time, fuel, and allows timely sowing.", "Sowing & Field Preparation"),
    ("How to manage heavy rice stubble before sowing wheat?", "Use a rotavator or a happy seeder to incorporate or manage the stubble instead of burning it, which depletes organic matter and causes smog.", "Sowing & Field Preparation"),

    # Seed Treatment & Varieties (15)
    ("Why is seed treatment important for wheat?", "Seed treatment with fungicides protects the crop against seed-borne diseases like loose smut and bunts.", "Seed Treatment & Varieties"),
    ("Which fungicide is recommended for wheat seed treatment?", "Treat seeds with systemic fungicides like Thiophanate-methyl, Carboxin, or Tebuconazole at 2 to 2.5 g/kg of seed.", "Seed Treatment & Varieties"),
    ("Can we mix insecticide with fungicide for seed treatment?", "Yes, adding Imidacloprid (3 ml/kg seed) can protect the early crop from sucking pests like aphids and termites.", "Seed Treatment & Varieties"),
    ("What are the highly recommended wheat varieties for Punjab?", "Popular varieties include Akbar-2019, Dilkash-20, Urooj-22, Bhakkar-20, and Anaj-17.", "Seed Treatment & Varieties"),
    ("Which wheat varieties are suitable for Sindh?", "Varieties like TD-1, Kiran-95, Benazir, and TJ-83 perform very well in the warmer climate of Sindh.", "Seed Treatment & Varieties"),
    ("What are the best varieties for rainfed (Barani) areas?", "Chakwal-50, Barani-17, and Pakistan-13 are highly recommended due to their drought tolerance.", "Seed Treatment & Varieties"),
    ("What varieties are recommended for late sowing (December)?", "Short-duration varieties like Zincol-2016 and Faisalabad-2008 are better suited for late sowing as they mature faster.", "Seed Treatment & Varieties"),
    ("How often should farmers replace their wheat seed?", "Farmers should replace their seed every 3 to 4 years to maintain genetic purity, vigor, and disease resistance.", "Seed Treatment & Varieties"),
    ("What is the germination percentage of good quality wheat seed?", "Certified wheat seed should have a germination percentage of at least 85%.", "Seed Treatment & Varieties"),
    ("How to test the germination rate of wheat seed at home?", "Place 100 seeds on moist tissue paper or sand in a warm place. After 5-7 days, count the sprouted seeds. If 85+ sprout, the seed is good.", "Seed Treatment & Varieties"),
    ("What is Zincol-2016 known for?", "Zincol-2016 is a biofortified variety enriched with higher levels of Zinc, beneficial for human health.", "Seed Treatment & Varieties"),
    ("Are there any rust-resistant varieties available?", "Yes, newer varieties like Akbar-2019 and Urooj-22 have high resistance against yellow and leaf rusts.", "Seed Treatment & Varieties"),
    ("Why should a farmer avoid sowing unapproved varieties?", "Unapproved varieties are often susceptible to diseases like rust and may have poor yield or grain quality under local conditions.", "Seed Treatment & Varieties"),
    ("How to clean farm-saved seed before sowing?", "Pass the seed through a standard seed grader to remove weed seeds, shriveled grains, and inert matter.", "Seed Treatment & Varieties"),
    ("What is the difference between certified seed and farm-saved seed?", "Certified seed is treated, graded, genetically pure, and guaranteed for high germination, while farm-saved seed may carry diseases and weed seeds.", "Seed Treatment & Varieties"),

    # Fertilizer Management (16)
    ("What is the general NPK recommendation for irrigated wheat?", "The general recommendation is 1 bag of DAP (Di-ammonium Phosphate) and 2 bags of Urea per acre.", "Fertilizer Management"),
    ("When should DAP be applied to the wheat crop?", "The entire dose of DAP (Phosphorus) must be applied at the time of sowing (basal dose) to promote strong root development.", "Fertilizer Management"),
    ("How should Urea be split in wheat?", "Urea is usually split: half at the time of the first irrigation (20-25 days after sowing) and the remaining half at the second irrigation.", "Fertilizer Management"),
    ("What is the fertilizer dose for rainfed (Barani) wheat?", "In Barani areas, apply half a bag of DAP and 1 bag of Urea per acre at the time of sowing, depending on soil moisture.", "Fertilizer Management"),
    ("Is Potassium (Potash) required for wheat?", "Yes, applying 1 bag of SOP (Sulphate of Potash) per acre at sowing improves grain weight, drought tolerance, and stem strength.", "Fertilizer Management"),
    ("How can Zinc deficiency be corrected in wheat?", "Apply 10 kg of 33% Zinc Sulphate per acre at the time of the first irrigation, especially if wheat follows a rice crop.", "Fertilizer Management"),
    ("What are the symptoms of Nitrogen deficiency in wheat?", "Older leaves turn pale yellow, plants become stunted, and tillering is severely reduced.", "Fertilizer Management"),
    ("What are the symptoms of Phosphorus deficiency?", "Plants grow slowly, and older leaves may develop a dark green or purplish tint. Root development is poor.", "Fertilizer Management"),
    ("Can we spray Urea on the wheat crop?", "Yes, a 2% Urea foliar spray (2 kg Urea dissolved in 100 liters of water) at the booting stage can boost grain protein and yield.", "Fertilizer Management"),
    ("Should I apply fertilizer if the crop is lodged?", "No, avoid applying Nitrogen (Urea) to a lodged crop, as it promotes vegetative growth and worsens lodging.", "Fertilizer Management"),
    ("Can Nitrophos (NP) be used instead of DAP?", "Yes, 2 bags of Nitrophos can replace 1 bag of DAP, as it provides both Nitrogen and Phosphorus, but you'll need to adjust the Urea dose.", "Fertilizer Management"),
    ("How does Sulphur application benefit wheat?", "Sulphur improves Nitrogen use efficiency and grain protein content. Use Ammonium Sulphate for one of your splits to provide Sulphur.", "Fertilizer Management"),
    ("What happens if Urea is applied too late (at flowering)?", "Late application of Nitrogen delays maturity, increases the risk of rust diseases, and causes lodging without significantly increasing yield.", "Fertilizer Management"),
    ("What is the role of Boron in wheat?", "Boron is critical for pollen viability and grain setting. Deficiency causes empty spikelets. Apply a foliar spray if soil is deficient.", "Fertilizer Management"),
    ("Is it beneficial to use bio-fertilizers in wheat?", "Yes, seed inoculation with Phosphobacteria and Azotobacter can fix atmospheric nitrogen and solubilize soil phosphorus.", "Fertilizer Management"),
    ("How to manage fertilizer in zero-tillage wheat?", "Use a zero-till drill with a dual hopper to place DAP fertilizer slightly below the seed in the same slit.", "Fertilizer Management"),

    # Weed Management (15)
    ("What is the critical period for weed control in wheat?", "Weeds should be controlled within the first 30 to 45 days after sowing to prevent yield loss.", "Weed Management"),
    ("What are the major broadleaf weeds in Pakistani wheat fields?", "Common broadleaf weeds include Bathu (Chenopodium album), Lehli (Convolvulus arvensis), and Piazi (Asphodelus tenuifolius).", "Weed Management"),
    ("What are the major narrow-leaf (grassy) weeds in wheat?", "Major grassy weeds are Dumbi Sitti (Phalaris minor) and Jangli Jai (Wild Oats).", "Weed Management"),
    ("When should post-emergence weedicides be sprayed?", "Spray weedicides when weeds are in the 2-4 leaf stage, usually after the first irrigation (30-40 days after sowing) when the soil is in 'Watter' condition.", "Weed Management"),
    ("What herbicide is used for broadleaf weeds?", "Herbicides like Tribenuron-methyl, Bromoxynil + MCPA, or 2,4-D are effective against broadleaf weeds.", "Weed Management"),
    ("What herbicide is used for grassy weeds?", "Use Clodinafop-propargyl, Fenoxaprop-p-ethyl, or Sulfosulfuron to control grassy weeds like Dumbi Sitti and Wild Oats.", "Weed Management"),
    ("Can we mix broadleaf and narrow-leaf herbicides together?", "Yes, broad-spectrum or 'ready-mix' herbicides like Atlantis (Mesosulfuron + Iodosulfuron) are available that kill both types of weeds.", "Weed Management"),
    ("Why shouldn't weedicides be sprayed in dry soil?", "Weedicides require soil moisture (Watter condition) to be absorbed effectively by the weed roots and leaves. Spraying in dry soil results in failure.", "Weed Management"),
    ("What time of day is best for spraying weedicides?", "Spray on a sunny, calm day after the morning dew has dried, usually between 10 AM and 3 PM.", "Weed Management"),
    ("What nozzle should be used for weedicide spray?", "Always use a Flat Fan nozzle or T-Jet nozzle for uniform coverage of weedicides.", "Weed Management"),
    ("How much water is needed per acre for a weedicide spray?", "Use 100 to 120 liters of clean water per acre to ensure complete coverage.", "Weed Management"),
    ("Is manual weeding possible in wheat?", "Manual weeding (hoeing) is effective but labor-intensive. It is practical for small farms or organic wheat cultivation.", "Weed Management"),
    ("What is herbicide resistance in Phalaris minor (Dumbi Sitti)?", "Overuse of the same herbicide (like Isoproturon) causes Dumbi Sitti to become resistant. Rotate herbicide chemistries every year to prevent this.", "Weed Management"),
    ("Does zero-tillage reduce weed problems?", "Yes, zero-tillage reduces the germination of Phalaris minor (Dumbi Sitti) because the soil is not disturbed.", "Weed Management"),
    ("How does crop rotation help in weed management?", "Rotating wheat with crops like berseem (fodder) or sunflower helps break the lifecycle of wheat-specific weeds like Wild Oats.", "Weed Management"),

    # Irrigation Management (15)
    ("How many irrigations are required for wheat in Pakistan?", "In the canal-irrigated plains, wheat generally requires 4 to 5 irrigations depending on winter rainfall.", "Irrigation Management"),
    ("What is the most critical stage for wheat irrigation?", "The Crown Root Initiation (CRI) stage, which occurs 20-25 days after sowing, is the most critical stage for irrigation.", "Irrigation Management"),
    ("What happens if the CRI stage irrigation is delayed?", "Delaying the first irrigation drastically reduces the formation of crown roots and tillers, severely decreasing the final yield.", "Irrigation Management"),
    ("When should the second irrigation be applied?", "The second irrigation is applied at the tillering to booting stage, around 50-60 days after sowing.", "Irrigation Management"),
    ("When is the third irrigation applied?", "The third irrigation is crucial at the flowering/heading stage, around 80-90 days after sowing.", "Irrigation Management"),
    ("When is the fourth irrigation applied?", "The fourth irrigation is applied at the grain-filling or milking stage (110-120 days), ensuring the grains become plump and heavy.", "Irrigation Management"),
    ("Should wheat be irrigated when strong winds are blowing?", "No, irrigating the crop during strong winds (especially in March/April) causes lodging, which severely damages the crop.", "Irrigation Management"),
    ("How to manage irrigation if there is an unexpected winter rain?", "If sufficient rainfall occurs (over 15-20 mm), skip or delay the scheduled irrigation.", "Irrigation Management"),
    ("Does bed planting save irrigation water?", "Yes, raising wheat on beds and irrigating the furrows saves up to 30-40% of water compared to flat flood irrigation.", "Irrigation Management"),
    ("What happens if the crop suffers drought stress at the milking stage?", "Water stress at the milking stage causes grains to shrivel, leading to lightweight grains and a massive drop in yield.", "Irrigation Management"),
    ("How to irrigate in areas with brackish ground water?", "Mix the brackish water with canal water, apply gypsum to the soil, and ensure proper leaching to prevent salt buildup.", "Irrigation Management"),
    ("Can sprinkler irrigation be used for wheat?", "Yes, sprinkler irrigation is highly efficient for wheat, especially in sandy soils or undulating terrain.", "Irrigation Management"),
    ("Is it harmful if water stagnates in the wheat field?", "Yes, standing water cuts off oxygen to the roots, turning the crop yellow. Wheat cannot tolerate waterlogging for more than 24-48 hours.", "Irrigation Management"),
    ("When should the final irrigation be stopped?", "Stop irrigation about 15-20 days before harvest to allow the crop to mature and dry properly.", "Irrigation Management"),
    ("How does a pre-sowing irrigation (Rauni) help?", "Rauni provides a deep moisture profile, allowing seeds to germinate uniformly and sustain the plant until the CRI stage.", "Irrigation Management"),

    # Pest Management (15)
    ("What are the major insect pests of wheat in Pakistan?", "The primary pests are Aphids, Armyworms, Termites, and Rodents (Rats).", "Pest Management"),
    ("How to identify an aphid attack on wheat?", "Aphids are small, green/black insects that cluster on the leaves and ears, sucking sap and secreting sticky honeydew.", "Pest Management"),
    ("At what stage do aphids attack wheat?", "Aphids typically attack from late February to March during the heading and grain-filling stages.", "Pest Management"),
    ("What is the Economic Threshold Level (ETL) for spraying against aphids?", "Spray only when there are more than 15 aphids per ear or plant, and natural predators (like ladybird beetles) are absent.", "Pest Management"),
    ("Which insecticides are effective against aphids?", "Safe insecticides like Imidacloprid, Thiamethoxam, or Flonicamid are effective. Avoid broad-spectrum sprays that kill beneficial insects.", "Pest Management"),
    ("How to control the armyworm in wheat fields?", "Armyworms eat leaves from the margins. Spray Emamectin Benzoate or Lufenuron in the evening, as caterpillars feed at night.", "Pest Management"),
    ("How to protect the wheat crop from termites?", "Treat seeds with Imidacloprid before sowing. If attacked later, flush Chlorpyrifos with the irrigation water.", "Pest Management"),
    ("What attracts termites to the wheat field?", "Undecomposed Farm Yard Manure or dry crop residues in sandy soils attract termites.", "Pest Management"),
    ("How to control rats in the wheat crop?", "Rats cut the tillers and eat grains. Clean the field boundaries and place Zinc Phosphide baits near their burrows.", "Pest Management"),
    ("What is the formula for Zinc Phosphide rat bait?", "Mix 1 part Zinc Phosphide, 1 part cooking oil, 1 part sugar/gur, and 40 parts crushed wheat grain.", "Pest Management"),
    ("Can burrow fumigation be used for rats?", "Yes, placing an Aluminum Phosphide (Phostoxin) tablet deep into active burrows and sealing them with wet mud is highly effective.", "Pest Management"),
    ("What are the signs of a shoot fly attack?", "Shoot flies cause 'dead hearts' in young seedlings, where the central shoot dries up and can be pulled out easily.", "Pest Management"),
    ("How to manage shoot flies in wheat?", "Timely sowing and a slightly higher seed rate mitigate shoot fly damage. In severe cases, apply granular insecticides.", "Pest Management"),
    ("Are there any bird pests for wheat?", "Sparrows and parrots can cause damage at the dough stage. Traditional scaring methods or reflective ribbons are used for deterrence.", "Pest Management"),
    ("Why are ladybird beetles important in the wheat field?", "Ladybird beetles and their larvae are natural predators that aggressively eat aphids. If you see them, avoid spraying pesticides.", "Pest Management"),

    # Disease Management (15)
    ("What is Yellow Rust (Stripe Rust) in wheat?", "Yellow Rust is a fungal disease appearing as yellow, powdery stripes on the leaves. It is a major threat in cooler, humid regions.", "Disease Management"),
    ("What is Leaf Rust (Brown Rust)?", "Leaf Rust appears as small, circular, brown/orange powdery pustules scattered randomly on the upper surface of the leaves.", "Disease Management"),
    ("What is Stem Rust (Black Rust)?", "Stem Rust forms dark reddish-brown to black elongated pustules on the stems and leaf sheaths. It occurs late in the season.", "Disease Management"),
    ("How to control rust diseases in wheat?", "The best strategy is to plant approved rust-resistant varieties like Akbar-2019. If symptoms appear, spray fungicides like Propiconazole or Tebuconazole.", "Disease Management"),
    ("When does yellow rust usually attack in Pakistan?", "Yellow rust typically appears in February and March when temperatures are between 10-20°C with high humidity.", "Disease Management"),
    ("What is Loose Smut in wheat?", "Loose Smut is a seed-borne fungal disease where the entire ear (spike) turns into a mass of black, powdery spores.", "Disease Management"),
    ("How to control Loose Smut?", "Since the fungus lives inside the seed, foliar sprays don't work. The only cure is seed treatment with systemic fungicides before sowing.", "Disease Management"),
    ("What is Karnal Bunt?", "Karnal Bunt replaces a portion of the grain with a black powdery mass that smells like rotting fish.", "Disease Management"),
    ("How to manage Karnal Bunt?", "Avoid using seed from infected areas, practice crop rotation, and spray fungicides (like Propiconazole) at the heading stage if the disease is endemic.", "Disease Management"),
    ("What causes Leaf Blight in wheat?", "Leaf Blight is caused by fungi (like Bipolaris or Alternaria), producing oval, brown spots with yellow halos on the leaves.", "Disease Management"),
    ("How to control Leaf Blight?", "Use disease-free seed, avoid excessive nitrogen, and apply broad-spectrum fungicides like Mancozeb or Azoxystrobin.", "Disease Management"),
    ("What is Powdery Mildew in wheat?", "It appears as a white to gray powdery fungal growth on the upper surface of the leaves in dense, highly fertilized fields.", "Disease Management"),
    ("How to manage Powdery Mildew?", "Avoid overcrowding by using the correct seed rate, do not over-apply Urea, and spray Sulphur-based fungicides.", "Disease Management"),
    ("What causes Foot Rot or Root Rot?", "Soil-borne fungi cause the roots and lower stems to rot, leading to stunted and yellow plants. Seed treatment is the primary defense.", "Disease Management"),
    ("Can a diseased crop be fed to livestock?", "Canes or plants infected with rusts can be fed, but grains infected with bunts or ergot may be toxic to livestock and humans.", "Disease Management"),

    # Harvesting, Storage & Miscellaneous (14)
    ("When is the right time to harvest wheat?", "Harvest when the grains are hard, the moisture content drops below 12-14%, and the straw turns golden yellow.", "Harvesting, Storage & Miscellaneous"),
    ("What happens if wheat is harvested too early?", "Early harvesting results in shriveled grains with high moisture, making them susceptible to fungal rotting during storage.", "Harvesting, Storage & Miscellaneous"),
    ("What happens if harvesting is delayed?", "Delaying the harvest increases the risk of grain shattering (falling to the ground) and damage from rain, wind, or birds.", "Harvesting, Storage & Miscellaneous"),
    ("Can combine harvesters be used for wheat?", "Yes, combine harvesters cut, thresh, and clean the grain simultaneously, saving immense labor and time.", "Harvesting, Storage & Miscellaneous"),
    ("What is the optimal grain moisture level for long-term storage?", "Wheat grains should be sun-dried until the moisture content is reduced to 10-12% before storage.", "Harvesting, Storage & Miscellaneous"),
    ("How to protect stored wheat from the Khapra beetle?", "Store wheat in airtight bins (Bhrolas) or sealed gunny bags. Use Aluminum Phosphide (Phostoxin/Agtoxin) tablets for fumigation.", "Harvesting, Storage & Miscellaneous"),
    ("What is the correct dosage of Phostoxin for stored wheat?", "Use 2 to 3 tablets per ton of wheat. Ensure the storage container is completely airtight so the poisonous gas doesn't leak.", "Harvesting, Storage & Miscellaneous"),
    ("How long should the storage container remain sealed after fumigation?", "The container must remain completely sealed for at least 7 to 10 days to kill all life stages of the insects.", "Harvesting, Storage & Miscellaneous"),
    ("Is it safe to mix neem leaves with stored wheat?", "Yes, mixing dried neem leaves is a traditional, safe, and organic method to deter storage pests without using chemicals.", "Harvesting, Storage & Miscellaneous"),
    ("How does smog affect the wheat crop?", "Smog blocks sunlight, reducing photosynthesis and resulting in slower plant growth and delayed maturity.", "Harvesting, Storage & Miscellaneous"),
    ("Why is burning wheat stubble harmful?", "Burning stubble destroys beneficial soil microbes, burns organic matter, releases greenhouse gases, and causes severe smog.", "Harvesting, Storage & Miscellaneous"),
    ("What should be done with wheat straw (Bhoosa)?", "Wheat straw is an essential dry fodder for livestock. It can be collected using a straw reaper and stored dry.", "Harvesting, Storage & Miscellaneous"),
    ("What is the average yield of wheat per acre in Pakistan?", "The national average is around 30-35 maunds per acre, but progressive farmers easily achieve 50-60 maunds using modern practices.", "Harvesting, Storage & Miscellaneous"),
    ("How can crop rotation increase wheat yield?", "Rotating wheat with leguminous crops like mung bean, berseem, or peas naturally adds nitrogen to the soil, boosting the subsequent wheat yield.", "Harvesting, Storage & Miscellaneous"),
    # --- Deep Agronomy: Zero Tillage & Happy Seeder ---
    ("What is Zero Tillage (ZT) technology in wheat farming?", "Zero Tillage involves sowing wheat directly into unploughed soil using a specialized ZT drill, immediately after the rice harvest, saving time, fuel, and preserving soil moisture.", "Advanced Agronomy"),
    ("What is the difference between a conventional drill and a Happy Seeder?", "A conventional drill requires cleared fields, whereas a Happy Seeder cuts standing rice stubble, sows the wheat seed in the soil, and spreads the chopped stubble over the sown area as mulch.", "Advanced Agronomy"),
    ("Why is the Happy Seeder critical for combating smog in Punjab?", "By managing heavy rice residues mechanically and converting them into mulch, the Happy Seeder completely eliminates the need for farmers to burn crop residues, the primary cause of winter smog.", "Advanced Agronomy"),
    ("What is Bed Planting for wheat?", "Bed planting involves sowing wheat on raised beds instead of flat land. It improves water use efficiency by 30-40%, reduces crusting, and minimizes lodging during heavy rains.", "Advanced Agronomy"),
    ("Can wheat be broadcasted in zero tillage conditions?", "No, broadcasting seed in unploughed, stubble-filled fields results in massive bird predation, poor seed-to-soil contact, and erratic germination. A drill is mandatory.", "Advanced Agronomy"),
    ("How does mulching with a Happy Seeder affect weed growth?", "The thick layer of chopped rice straw mulch acts as a physical barrier that drastically suppresses the emergence of troublesome weeds like Phalaris minor (Dumbi Sitti).", "Advanced Agronomy"),

    # --- Specific Weed Resistance & Herbicides ---
    ("What is herbicide resistance in wheat weeds?", "It is the evolved ability of weeds (like Phalaris minor) to survive chemical sprays that previously killed them, usually caused by farmers repeatedly using the same herbicide year after year.", "Weed Management"),
    ("Why did Isoproturon fail to control weeds in the rice-wheat belt?", "Continuous use of Isoproturon over decades caused Phalaris minor to develop severe genetic resistance, rendering the chemical completely ineffective in central Punjab.", "Weed Management"),
    ("What is the recommended alternative to Isoproturon for grassy weeds?", "Farmers must rotate chemistries and use modern herbicides like Clodinafop-propargyl, Fenoxaprop-p-ethyl (Puma Super), or Pinoxaden (Axial) to manage resistant Phalaris minor.", "Weed Management"),
    ("What is 'tank mixing' of herbicides?", "It is the practice of mixing a broadleaf herbicide (e.g., Bromoxynil) and a grassy weed herbicide (e.g., Clodinafop) in the same spray tank to control all weeds in a single pass.", "Weed Management"),
    ("Is it safe to tank-mix any two herbicides for wheat?", "No. Certain mixtures can cause severe phytotoxicity (crop burning) or chemical antagonism (where one chemical neutralizes the other). Always consult the manufacturer's label before mixing.", "Weed Management"),
    ("At what precise leaf stage should post-emergence weedicides be applied in wheat?", "They must be applied when weeds are actively growing at the 2 to 4-leaf stage, typically 30 to 45 days after sowing, right after the first irrigation.", "Weed Management"),

    # --- Deep Pathology: Smut, Rusts, & Bunt ---
    ("What is the exact life cycle of Loose Smut in wheat?", "The fungus infects the flower during flowering. It remains dormant inside the seed embryo. When the infected seed is planted next year, the fungus grows internally with the plant, replacing the new ear with black spores.", "Disease Management"),
    ("Can a farmer visibly identify a Loose Smut-infected seed before sowing?", "No, the infected seed looks completely healthy and normal from the outside. The only way to prevent it is by treating all seeds with a systemic fungicide like Triadimenol before sowing.", "Disease Management"),
    ("What is Karnal Bunt and why is it an economic disaster?", "Karnal Bunt is a fungal disease that partially hollows out the grain, leaving a black powdery mass that smells like rotting fish. Even a 1-2% infection can cause entire export shipments to be rejected.", "Disease Management"),
    ("How does Karnal Bunt spread?", "It is a soil-borne and air-borne disease. The spores survive in the soil for up to 5 years and infect the wheat heads during light rains at the flowering stage.", "Disease Management"),
    ("What is the Ug99 strain of Stem Rust?", "Ug99 is a highly virulent, mutant strain of stem rust discovered in Uganda that can overcome the resistance genes present in most of the world's wheat varieties, posing a severe threat to global food security.", "Disease Management"),
    ("How does Pakistan protect against Ug99 and other new rust strains?", "Agricultural research institutes constantly breed and release new rust-resistant varieties (like Akbar-19, Ujala-16) and aggressively phase out older susceptible varieties (like Inqilab-91).", "Disease Management"),
    ("What is Black Point disease in wheat?", "It is a fungal infection (usually Alternaria or Bipolaris) causing the germ end of the grain to turn dark black or brown, usually triggered by heavy rains just before harvest, reducing market grade.", "Disease Management"),

    # --- Harvesting Machinery & Shattering Losses ---
    ("What causes grain shattering in mature wheat?", "Over-ripening, delays in harvesting, strong dry winds, and specific varietal traits cause the glumes to open and drop the grain directly onto the ground, causing massive yield loss.", "Harvesting & Machinery"),
    ("How to properly calibrate a combine harvester for wheat?", "The reel speed must match the forward speed, the cutter bar must be sharp, and the concave clearance and fan speed must be adjusted according to the grain moisture to prevent crushing or blowing grain out the back.", "Harvesting & Machinery"),
    ("Why is night harvesting with combine harvesters common but discouraged?", "Farmers harvest at night to avoid the daytime heat, but the nighttime dew increases grain moisture, causing the thresher to choke and resulting in poorly threshed, high-moisture grain that rots in storage.", "Harvesting & Machinery"),
    ("What is a Reaper-Binder?", "It is a machine that cuts the wheat stalks and automatically ties them into bundles (sheaves), which are then left in the field to dry before stationary threshing. It is useful for smaller farms.", "Harvesting & Machinery"),
    ("How is the wheat straw (Toodi) recovered after combine harvesting?", "Combine harvesters leave tall stubble and drop chopped straw. Farmers must use a specialized tractor-mounted 'Straw Reaper' or 'Chopper' to collect, chop, and blow the straw into a trolley for animal feed.", "Harvesting & Machinery"),

    # --- Storage Structures & Fumigation ---
    ("What is a 'Bukhari' in traditional Pakistani grain storage?", "A Bukhari is a traditional, indoor, unsealed storage bin made of mud, straw, and cow dung. It is highly susceptible to rodent attacks and moisture penetration.", "Storage & Fumigation"),
    ("What are 'Passu' bins?", "Passu bins are modern, galvanized iron, airtight storage silos distributed by the government and NGOs to smallholder farmers to drastically reduce post-harvest losses from pests and moisture.", "Storage & Fumigation"),
    ("What is the chemical name of the fumigant used for stored wheat?", "Aluminum Phosphide, commercially sold under brand names like Phostoxin or Celphos.", "Storage & Fumigation"),
    ("How does Aluminum Phosphide work in a grain silo?", "When the solid tablets are exposed to air moisture, they undergo a chemical reaction to release Phosphine (PH3) gas, which is highly toxic and permeates the grain to kill all insects, larvae, and eggs.", "Storage & Fumigation"),
    ("What is the most critical safety requirement when using Phosphine tablets?", "The storage structure MUST be completely airtight (sealed with mud or plastic). If it leaks, the gas escapes, failing to kill pests, and posing a lethal inhalation risk to humans and livestock nearby.", "Storage & Fumigation"),
    ("Why should farmers never mix synthetic pesticide dust directly into stored wheat meant for human consumption?", "Pesticide dusts leave toxic chemical residues that cannot be washed off or destroyed by cooking, leading to severe chronic health issues. Only gas fumigants (which leave no residue) should be used.", "Storage & Fumigation"),
    ("How to control the Khapra beetle (Trogoderma granarium)?", "The Khapra beetle is the most destructive storage pest and is highly resistant to many chemicals. Strict airtight fumigation with high-dose Phosphine gas for at least 7-10 days is required.", "Storage & Fumigation"),

    # --- Economics: PASSCO, Procurement, & Support Price ---
    ("What is PASSCO's role in the Pakistani wheat sector?", "The Pakistan Agricultural Storage and Services Corporation (PASSCO) is the federal agency responsible for procuring wheat directly from farmers to maintain strategic national reserves and stabilize prices.", "Economics & Marketing"),
    ("What is the 'Support Price' for wheat?", "It is a minimum guaranteed price announced by the government before or during the harvest to ensure farmers recover their production costs and are protected from sudden market crashes.", "Economics & Marketing"),
    ("What is 'Bardana' and why is it a contentious issue?", "Bardana refers to the jute or woven polypropylene bags issued by the government to farmers for packing wheat. Distribution is often marred by bureaucratic delays and corruption, forcing small farmers to sell to middlemen at lower prices.", "Economics & Marketing"),
    ("How does the 'Middleman' (Arthi) operate in the wheat supply chain?", "The Arthi provides informal, high-interest credit (seeds, fertilizer) to farmers during the growing season on the strict condition that the farmer must sell the harvested wheat exclusively to the Arthi, usually below the government support price.", "Economics & Marketing"),
    ("What is the economic impact of delayed wheat sowing?", "Research shows that for every single day wheat sowing is delayed beyond November 20th in Punjab, the potential yield drops by 1% (roughly 15-20 kg per acre) due to the shortened grain-filling period before the intense spring heat.", "Economics & Marketing"),

    # --- Minor Nutrients & Specific Soils ---
    ("How does Manganese deficiency manifest in wheat?", "Manganese deficiency is common in sandy, over-limed soils. It causes 'interveinal chlorosis' (yellowing between the veins) on younger leaves, while the veins remain distinctly green.", "Soil & Nutrition"),
    ("What is the impact of soil salinity on wheat germination?", "High salt concentrations create an osmotic barrier, preventing the seed from absorbing water. This causes delayed, patchy, or completely failed germination.", "Soil & Nutrition"),
    ("How can a farmer successfully grow wheat in moderately saline (Kallar) soils?", "Use salt-tolerant varieties (like Pasban-90 or S-24), increase the seed rate by 20%, apply heavy pre-sowing irrigation to leach salts below the root zone, and use acidic fertilizers like Ammonium Sulphate instead of standard Urea.", "Soil & Nutrition"),
    ("Why is Sulphur becoming deficient in Pakistani wheat fields?", "The historical shift from Sulphur-containing fertilizers (like Single Super Phosphate) to highly concentrated, Sulphur-free fertilizers (like DAP and Urea) has depleted soil Sulphur over decades.", "Soil & Nutrition"),
    ("How to correct Sulphur deficiency in wheat?", "Apply Elemental Sulphur, use Ammonium Sulphate, or use Sulphate of Potash (SOP) to ensure the crop has enough Sulphur for protein synthesis and grain quality.", "Soil & Nutrition")
]

filename = 'Pakistan_Wheat_QA.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} wheat queries successfully!")
