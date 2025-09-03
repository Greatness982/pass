import streamlit as st
import random
import json
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="EduQuiz - Educational Quiz App",
    page_icon="📚",
    layout="wide"
)

# Sample educational content - past questions for Primary 2 to SS3
educational_content = {
    "Primary 2": {
        "Social Studies": {
            "Family": [
                {"question": "Who is the head of the family?", "options": ["Father", "Mother", "Child", "Uncle"], "answer": "Father"},
                {"question": "Who cooks most times at home?", "options": ["Mother", "Father", "Brother", "Cousin"], "answer": "Mother"},
                {"question": "What do we call father and mother together?", "options": ["Children", "Parents", "Friends", "Family"], "answer": "Parents"},
                {"question": "Who are brothers and sisters?", "options": ["Cousins", "Parents", "Siblings", "Friends"], "answer": "Siblings"},
                {"question": "Who is your mother's mother?", "options": ["Aunt", "Sister", "Grandmother", "Niece"], "answer": "Grandmother"}
            ],
            "Culture": [
                {"question": "What do we wear on our body?", "options": ["Food", "Clothes", "Shoes", "Books"], "answer": "Clothes"},
                {"question": "Which one is a Nigerian traditional food?", "options": ["Pizza", "Rice", "Eba", "Burger"], "answer": "Eba"},
                {"question": "Drums are used for?", "options": ["Cooking", "Dancing", "Eating", "Sleeping"], "answer": "Dancing"},
                {"question": "What do people use to cover their heads in Hausa culture?", "options": ["Cap", "Shoes", "Glasses", "Book"], "answer": "Cap"},
                {"question": "Which one is a festival?", "options": ["Eid", "Christmas", "New Yam", "All of the above"], "answer": "All of the above"}
            ],
            "Government": [
                {"question": "Who is the leader of a school?", "options": ["Teacher", "Head teacher", "Prefect", "Parent"], "answer": "Head teacher"},
                {"question": "Who leads a state?", "options": ["Governor", "President", "Chairman", "Teacher"], "answer": "Governor"},
                {"question": "Who is the leader of Nigeria?", "options": ["Senator", "President", "Minister", "Governor"], "answer": "President"},
                {"question": "Who leads a local government?", "options": ["Chairman", "Teacher", "King", "Driver"], "answer": "Chairman"},
                {"question": "Who makes laws in Nigeria?", "options": ["Students", "National Assembly", "Teachers", "Farmers"], "answer": "National Assembly"}
            ],
            "Values": [
                {"question": "What should we say when someone gives us something?", "options": ["Thanks", "Sorry", "Yes", "Good"], "answer": "Thanks"},
                {"question": "Which is a good habit?", "options": ["Stealing", "Fighting", "Greeting elders", "Lying"], "answer": "Greeting elders"},
                {"question": "What should we do with rubbish?", "options": ["Throw on the floor", "Burn anywhere", "Put in a bin", "Hide it"], "answer": "Put in a bin"},
                {"question": "Which one is bad behavior?", "options": ["Helping others", "Obeying parents", "Lying", "Studying"], "answer": "Lying"},
                {"question": "What should we say when we offend someone?", "options": ["Goodbye", "Welcome", "Sorry", "Hello"], "answer": "Sorry"}
            ]
        },
        "Civic Education": {
            "Rights": [
                {"question": "Children have the right to?", "options": ["Play", "Education", "Sleep", "All of the above"], "answer": "All of the above"},
                {"question": "Which is a child's right?", "options": ["Right to school", "Right to fight", "Right to steal", "Right to cheat"], "answer": "Right to school"},
                {"question": "Right to life means?", "options": ["We should live", "We should die", "We should fight", "We should sleep"], "answer": "We should live"},
                {"question": "Children should not be?", "options": ["Cared for", "Protected", "Abused", "Loved"], "answer": "Abused"},
                {"question": "Which is NOT a child's right?", "options": ["Right to food", "Right to medicine", "Right to lying", "Right to play"], "answer": "Right to lying"}
            ],
            "Duties": [
                {"question": "Children should ___ their parents.", "options": ["Obey", "Fight", "Ignore", "Steal from"], "answer": "Obey"},
                {"question": "We must ___ in school.", "options": ["Learn", "Sleep", "Fight", "Run"], "answer": "Learn"},
                {"question": "We must respect our ___?", "options": ["Teachers", "Friends", "Parents", "All of the above"], "answer": "All of the above"},
                {"question": "We should keep our environment?", "options": ["Dirty", "Clean", "Ugly", "Bad"], "answer": "Clean"},
                {"question": "Children must not ___?", "options": ["Help", "Steal", "Respect", "Learn"], "answer": "Steal"}
            ],
            "Good Behavior": [
                {"question": "Which is a sign of respect?", "options": ["Greeting elders", "Fighting", "Lying", "Stealing"], "answer": "Greeting elders"},
                {"question": "What should we do before eating?", "options": ["Pray", "Sleep", "Run", "Fight"], "answer": "Pray"},
                {"question": "When someone is talking, we should?", "options": ["Listen", "Shout", "Sleep", "Fight"], "answer": "Listen"},
                {"question": "We should always speak the?", "options": ["Truth", "Lie", "Noise", "Secret"], "answer": "Truth"},
                {"question": "Good children must always be?", "options": ["Respectful", "Lazy", "Rude", "Fighting"], "answer": "Respectful"}
            ]
        },
        "CRS/IRS": {
            "Bible/Quran Stories": [
                {"question": "Who created the world?", "options": ["God", "Man", "Animals", "Sun"], "answer": "God"},
                {"question": "Who built the ark?", "options": ["Moses", "Noah", "Abraham", "David"], "answer": "Noah"},
                {"question": "Who led Israelites out of Egypt?", "options": ["Moses", "Joseph", "David", "Peter"], "answer": "Moses"},
                {"question": "In Islam, who is the last prophet?", "options": ["Isa", "Musa", "Muhammad", "Ibrahim"], "answer": "Muhammad"},
                {"question": "Muslims pray ___ times a day.", "options": ["2", "3", "5", "7"], "answer": "5"}
            ],
            "Morals": [
                {"question": "We must not?", "options": ["Pray", "Steal", "Obey", "Respect"], "answer": "Steal"},
                {"question": "We should always?", "options": ["Lie", "Tell the truth", "Fight", "Hate"], "answer": "Tell the truth"},
                {"question": "Which is a good moral?", "options": ["Kindness", "Stealing", "Fighting", "Cheating"], "answer": "Kindness"},
                {"question": "We should always pray to?", "options": ["God", "Man", "Angels", "Animals"], "answer": "God"},
                {"question": "In Christianity, who is the son of God?", "options": ["Abraham", "Isaac", "Jesus", "David"], "answer": "Jesus"}
            ]
        }
    },
    "Primary 5": {
        "Social Studies": {
            "Nigeria": [
                {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Ibadan"], "answer": "Abuja"},
                {"question": "Who is the head of Nigeria?", "options": ["Governor", "President", "Minister", "Chairman"], "answer": "President"},
                {"question": "Nigeria is in which continent?", "options": ["Asia", "Europe", "Africa", "America"], "answer": "Africa"},
                {"question": "What are the three major ethnic groups in Nigeria?", "options": ["Hausa, Yoruba, Igbo", "Fulani, Edo, Ijaw", "Kanuri, Tiv, Nupe", "None"], "answer": "Hausa, Yoruba, Igbo"},
                {"question": "The Nigerian flag is?", "options": ["Green-White-Green", "Red-White-Blue", "Black-White", "Green-Yellow"], "answer": "Green-White-Green"}
            ],
            "Economy": [
                {"question": "Nigeria's main source of income is?", "options": ["Oil", "Gold", "Cocoa", "Timber"], "answer": "Oil"},
                {"question": "Which one is a cash crop?", "options": ["Yam", "Rice", "Cocoa", "Beans"], "answer": "Cocoa"},
                {"question": "Which one is NOT an occupation?", "options": ["Farming", "Fishing", "Trading", "Sleeping"], "answer": "Sleeping"},
                {"question": "Farmers grow food in?", "options": ["Factories", "Markets", "Farms", "Offices"], "answer": "Farms"},
                {"question": "Which one is a service job?", "options": ["Teacher", "Farmer", "Hunter", "Fisherman"], "answer": "Teacher"}
            ],
            "Government": [
                {"question": "Who leads a state?", "options": ["Governor", "Chairman", "Minister", "President"], "answer": "Governor"},
                {"question": "Who makes laws?", "options": ["Teachers", "National Assembly", "Parents", "Farmers"], "answer": "National Assembly"},
                {"question": "Nigeria has how many states?", "options": ["30", "32", "36", "40"], "answer": "36"},
                {"question": "Which is the local government head?", "options": ["Chairman", "Governor", "Minister", "King"], "answer": "Chairman"},
                {"question": "Who controls the army?", "options": ["Governor", "Teacher", "President", "Headmaster"], "answer": "President"}
            ]
        },
        "Civic Education": {
            "Democracy": [
                {"question": "Democracy means?", "options": ["Rule by the people", "Rule by one person", "Rule by soldiers", "Rule by kings"], "answer": "Rule by the people"},
                {"question": "Which is a democratic country?", "options": ["Nigeria", "China (one party)", "North Korea", "None"], "answer": "Nigeria"},
                {"question": "Voting is done during?", "options": ["Election", "Party", "School", "Market"], "answer": "Election"},
                {"question": "Leaders in democracy are chosen by?", "options": ["Fighting", "Voting", "Inheritance", "Luck"], "answer": "Voting"},
                {"question": "Which is NOT part of democracy?", "options": ["Freedom", "Dictatorship", "Rights", "Participation"], "answer": "Dictatorship"}
            ],
            "Rights": [
                {"question": "Every child has right to?", "options": ["Education", "Sleep", "Fight", "Lie"], "answer": "Education"},
                {"question": "Right to vote belongs to?", "options": ["Adults", "Children", "Teachers", "Animals"], "answer": "Adults"},
                {"question": "Right to life means?", "options": ["We should live", "We should die", "We should fight", "We should sleep"], "answer": "We should live"},
                {"question": "Right to worship means?", "options": ["Pray to God", "Steal", "Fight", "Sleep"], "answer": "Pray to God"},
                {"question": "Which is NOT a right?", "options": ["Education", "Stealing", "Food", "Freedom"], "answer": "Stealing"}
            ],
            "Duties": [
                {"question": "Children must ___ their parents.", "options": ["Obey", "Fight", "Disrespect", "Ignore"], "answer": "Obey"},
                {"question": "Citizens must obey?", "options": ["Parents", "Laws", "Animals", "Children"], "answer": "Laws"},
                {"question": "Citizens must pay?", "options": ["Fines", "Bribes", "Taxes", "Debt"], "answer": "Taxes"},
                {"question": "Citizens must respect?", "options": ["Law", "Leaders", "Others", "All of the above"], "answer": "All of the above"},
                {"question": "Children must not ___?", "options": ["Steal", "Study", "Learn", "Respect"], "answer": "Steal"}
            ]
        },
        "CRS/IRS": {
            "Bible Stories": [
                {"question": "Who killed Goliath?", "options": ["Saul", "David", "Moses", "Joseph"], "answer": "David"},
                {"question": "Who was swallowed by a big fish?", "options": ["Jonah", "Moses", "Paul", "Peter"], "answer": "Jonah"},
                {"question": "Who was the mother of Jesus?", "options": ["Mary", "Elizabeth", "Ruth", "Sarah"], "answer": "Mary"},
                {"question": "Where was Jesus born?", "options": ["Nazareth", "Bethlehem", "Jerusalem", "Galilee"], "answer": "Bethlehem"},
                {"question": "Who betrayed Jesus?", "options": ["Peter", "John", "Judas", "Paul"], "answer": "Judas"}
            ],
            "Quran Stories": [
                {"question": "Who is the last prophet in Islam?", "options": ["Musa", "Isa", "Ibrahim", "Muhammad"], "answer": "Muhammad"},
                {"question": "Muslims pray how many times daily?", "options": ["3", "4", "5", "6"], "answer": "5"},
                {"question": "What is the holy book of Islam?", "options": ["Bible", "Torah", "Quran", "Hadith"], "answer": "Quran"},
                {"question": "During Ramadan, Muslims must?", "options": ["Fast", "Play", "Sleep", "Fight"], "answer": "Fast"},
                {"question": "The first pillar of Islam is?", "options": ["Salat", "Shahada", "Zakat", "Sawm"], "answer": "Shahada"}
            ],
            "Morals": [
                {"question": "We must always?", "options": ["Pray", "Lie", "Fight", "Steal"], "answer": "Pray"},
                {"question": "We must be?", "options": ["Kind", "Rude", "Selfish", "Lazy"], "answer": "Kind"},
                {"question": "We must not?", "options": ["Respect", "Steal", "Love", "Obey"], "answer": "Steal"},
                {"question": "Truth is better than?", "options": ["Lies", "Kindness", "Love", "Peace"], "answer": "Lies"},
                {"question": "Good children must?", "options": ["Respect elders", "Steal money", "Fight teachers", "Disobey parents"], "answer": "Respect elders"}
            ]
        }
    },
    "JSS 3": {
        "Mathematics": {
            "Algebra": [
                {"question": "Simplify: 2x + 3x", "options": ["5", "5x", "6x", "2"], "answer": "5x"},
                {"question": "If x=2, what is 3x + 4?", "options": ["6", "7", "10", "12"], "answer": "10"},
                {"question": "Expand: (x + 2)(x + 3)", "options": ["x²+5x+6", "x²+6x+5", "x²+3x+2", "x²+2x+3"], "answer": "x²+5x+6"},
                {"question": "Factorize: x² + 5x + 6", "options": ["(x+2)(x+3)", "(x+6)(x+5)", "(x+1)(x+6)", "(x+3)(x+5)"], "answer": "(x+2)(x+3)"},
                {"question": "Solve: 2x – 4 = 10", "options": ["x=6", "x=7", "x=5", "x=8"], "answer": "x=7"}
            ],
            "Geometry": [
                {"question": "Sum of angles in a triangle is?", "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
                {"question": "Area of a rectangle = ?", "options": ["l+b", "2l+2b", "l×b", "l–b"], "answer": "l×b"},
                {"question": "A straight line angle is?", "options": ["180°", "90°", "360°", "45°"], "answer": "180°"},
                {"question": "How many sides has a hexagon?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "Volume of a cube = ?", "options": ["a³", "2a", "4a", "6a"], "answer": "a³"}
            ],
            "Probability": [
                {"question": "Probability ranges between?", "options": ["0 and 100", "0 and 1", "1 and 10", "0 and 10"], "answer": "0 and 1"},
                {"question": "Tossing a fair coin, probability of head?", "options": ["1/4", "1/2", "1/3", "2/3"], "answer": "1/2"},
                {"question": "Rolling a die, probability of getting 5?", "options": ["1/6", "1/5", "1/4", "1/3"], "answer": "1/6"},
                {"question": "If P(E)=0, the event is?", "options": ["Certain", "Impossible", "Likely", "Unlikely"], "answer": "Impossible"},
                {"question": "Probability of an impossible event?", "options": ["1", "0", "0.5", "2"], "answer": "0"}
            ],
            "Trigonometry": [
                {"question": "sin²θ + cos²θ = ?", "options": ["0", "1", "2", "θ"], "answer": "1"},
                {"question": "tanθ = ?", "options": ["sinθ/cosθ", "cosθ/sinθ", "1/sinθ", "1/cosθ"], "answer": "sinθ/cosθ"},
                {"question": "If sinθ = 1, θ =", "options": ["0°", "90°", "180°", "360°"], "answer": "90°"},
                {"question": "cos 0° =", "options": ["0", "1", "-1", "0.5"], "answer": "1"},
                {"question": "tan 45° =", "options": ["0", "1", "-1", "∞"], "answer": "1"}
            ]
        },
        "English": {
            "Grammar": [
                {"question": "Pick the verb: The boy runs fast.", "options": ["boy", "runs", "fast", "the"], "answer": "runs"},
                {"question": "Which is correct?", "options": ["She go to school", "She goes to school", "She going to school", "She gone to school"], "answer": "She goes to school"},
                {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childes", "childrens"], "answer": "children"},
                {"question": "Which is an adjective?", "options": ["quickly", "beautiful", "run", "and"], "answer": "beautiful"},
                {"question": "Choose the correct pronoun: ___ is my friend.", "options": ["He", "Him", "His", "Her"], "answer": "He"}
            ],
            "Vocabulary": [
                {"question": "Synonym of 'happy'?", "options": ["sad", "angry", "joyful", "cry"], "answer": "joyful"},
                {"question": "Antonym of 'big'?", "options": ["large", "huge", "small", "giant"], "answer": "small"},
                {"question": "Which one is a noun?", "options": ["book", "run", "quickly", "beautiful"], "answer": "book"},
                {"question": "Choose the correct: I ___ a pen.", "options": ["has", "have", "having", "had"], "answer": "have"},
                {"question": "Which word means 'a place where books are kept'?", "options": ["market", "school", "library", "hospital"], "answer": "library"}
            ],
            "Literature": [
                {"question": "Who wrote 'Things Fall Apart'?", "options": ["Chinua Achebe", "Wole Soyinka", "Ngugi wa Thiong'o", "Ken Saro-Wiwa"], "answer": "Chinua Achebe"},
                {"question": "Poems are written in?", "options": ["Paragraphs", "Chapters", "Lines and stanzas", "Acts"], "answer": "Lines and stanzas"},
                {"question": "Drama is meant to be?", "options": ["Read", "Acted", "Sung", "Painted"], "answer": "Acted"},
                {"question": "Who is the main character in a story?", "options": ["Narrator", "Protagonist", "Villain", "Writer"], "answer": "Protagonist"},
                {"question": "A short story is called?", "options": ["Poem", "Novel", "Fable", "Play"], "answer": "Fable"}
            ],
            "Comprehension": [
                {"question": "Comprehension tests check your?", "options": ["Writing", "Speaking", "Understanding", "Drawing"], "answer": "Understanding"},
                {"question": "To skim a passage means?", "options": ["Read quickly", "Read slowly", "Memorize", "Forget"], "answer": "Read quickly"},
                {"question": "Main idea of a passage is?", "options": ["Title", "Central point", "First line", "Last line"], "answer": "Central point"},
                {"question": "Another word for 'summary' is?", "options": ["Detail", "Outline", "Essay", "Chapter"], "answer": "Outline"},
                {"question": "To infer means?", "options": ["Guess meaning", "Translate", "Copy", "Ignore"], "answer": "Guess meaning"}
            ]
        },
        "Basic Science": {
            "Physics Basics": [
                {"question": "Force is measured in?", "options": ["Newton", "Joule", "Watt", "Meter"], "answer": "Newton"},
                {"question": "Energy is the ability to?", "options": ["Work", "Sleep", "Run", "Eat"], "answer": "Work"},
                {"question": "The force of attraction between two objects is?", "options": ["Magnetism", "Gravity", "Friction", "Pressure"], "answer": "Gravity"},
                {"question": "Which one is NOT a type of energy?", "options": ["Heat", "Sound", "Light", "Chair"], "answer": "Chair"},
                {"question": "Work = ?", "options": ["Force × Distance", "Force ÷ Time", "Energy ÷ Distance", "Power × Time"], "answer": "Force × Distance"}
            ],
            "Chemistry Basics": [
                {"question": "The smallest particle of matter is?", "options": ["Atom", "Molecule", "Compound", "Element"], "answer": "Atom"},
                {"question": "H₂O is the formula for?", "options": ["Oxygen", "Water", "Hydrogen", "Acid"], "answer": "Water"},
                {"question": "NaCl is called?", "options": ["Sugar", "Salt", "Chalk", "Iron"], "answer": "Salt"},
                {"question": "Which is NOT a state of matter?", "options": ["Solid", "Liquid", "Gas", "Fire"], "answer": "Fire"},
                {"question": "Air is a?", "options": ["Element", "Compound", "Mixture", "Solution"], "answer": "Mixture"}
            ],
            "Biology Basics": [
                {"question": "The basic unit of life is?", "options": ["Organ", "Tissue", "Cell", "System"], "answer": "Cell"},
                {"question": "Plants make food by?", "options": ["Respiration", "Photosynthesis", "Digestion", "Fermentation"], "answer": "Photosynthesis"},
                {"question": "Which one is a vertebrate?", "options": ["Dog", "Snail", "Ant", "Worm"], "answer": "Dog"},
                {"question": "Blood in humans is pumped by?", "options": ["Lungs", "Brain", "Heart", "Kidney"], "answer": "Heart"},
                {"question": "Which organ helps in breathing?", "options": ["Heart", "Lungs", "Kidney", "Liver"], "answer": "Lungs"}
            ]
        },
        "Social Studies": {
            "Government": [
                {"question": "Who is the head of local government?", "options": ["Chairman", "Governor", "Minister", "President"], "answer": "Chairman"},
                {"question": "Nigeria practices what type of government?", "options": ["Democracy", "Monarchy", "Dictatorship", "Military"], "answer": "Democracy"},
                {"question": "Who makes laws?", "options": ["Police", "National Assembly", "Judges", "Teachers"], "answer": "National Assembly"},
                {"question": "The third arm of government is?", "options": ["Executive", "Judiciary", "Legislature", "Military"], "answer": "Judiciary"},
                {"question": "The Nigerian Constitution is a?", "options": ["Book of stories", "Book of laws", "Book of names", "Book of history"], "answer": "Book of laws"}
            ],
            "Economy": [
                {"question": "Money is used as?", "options": ["Toy", "Exchange", "Decoration", "Food"], "answer": "Exchange"},
                {"question": "Which one is a natural resource?", "options": ["Oil", "Car", "Computer", "House"], "answer": "Oil"},
                {"question": "Which is NOT an economic activity?", "options": ["Farming", "Fishing", "Trading", "Sleeping"], "answer": "Sleeping"},
                {"question": "The central bank of Nigeria is?", "options": ["CBN", "UBA", "First Bank", "GTB"], "answer": "CBN"},
                {"question": "Which is a form of trade without money?", "options": ["Barter", "Retail", "Wholesale", "Import"], "answer": "Barter"}
            ],
            "Culture": [
                {"question": "Culture means?", "options": ["Way of life", "Way of eating", "Way of fighting", "Way of schooling"], "answer": "Way of life"},
                {"question": "Which is part of culture?", "options": ["Dress", "Food", "Language", "All of the above"], "answer": "All of the above"},
                {"question": "The Yoruba traditional ruler is called?", "options": ["Oba", "Emir", "Obi", "King"], "answer": "Oba"},
                {"question": "Which tribe is known for masquerades?", "options": ["Igbo", "Yoruba", "Hausa", "Fulani"], "answer": "Igbo"},
                {"question": "Which is a Nigerian cultural festival?", "options": ["Durbar", "Thanksgiving", "Christmas", "Easter"], "answer": "Durbar"}
            ],
            "History": [
                {"question": "Nigeria got independence in?", "options": ["1960", "1963", "1970", "1957"], "answer": "1960"},
                {"question": "Who was Nigeria's first president?", "options": ["Nnamdi Azikiwe", "Tafawa Balewa", "Obasanjo", "Awolowo"], "answer": "Nnamdi Azikiwe"},
                {"question": "The first capital of Nigeria was?", "options": ["Lagos", "Abuja", "Kano", "Kaduna"], "answer": "Lagos"},
                {"question": "Nigeria fought a civil war in?", "options": ["1960-63", "1967-70", "1975-77", "1980-83"], "answer": "1967-70"},
                {"question": "Slave trade ended in Nigeria in?", "options": ["1807", "1900", "1914", "1960"], "answer": "1807"}
            ]
        }
    },
    "SSS 3": {
        "Mathematics": {
            "Algebra": [
                {"question": "Solve for x: 2x + 5 = 15", "options": ["5", "7.5", "10", "20"], "answer": "5"},
                {"question": "If x = 2, evaluate 3x² + 4", "options": ["16", "12", "20", "24"], "answer": "16"},
                {"question": "Expand (x + 2)(x + 3)", "options": ["x² + 6x + 5", "x² + 5x + 6", "x² + 2x + 3", "x² + 3x + 5"], "answer": "x² + 5x + 6"},
                {"question": "Simplify: (x² – 9) ÷ (x – 3)", "options": ["x – 3", "x + 3", "x² + 3", "x² – 3"], "answer": "x + 3"},
                {"question": "If 2x = 14, then x = ?", "options": ["5", "6", "7", "8"], "answer": "7"}
            ],
            "Geometry": [
                {"question": "Sum of angles in a triangle is?", "options": ["90°", "120°", "180°", "360°"], "answer": "180°"},
                {"question": "A straight line is equal to?", "options": ["90°", "180°", "360°", "45°"], "answer": "180°"},
                {"question": "Area of a circle = ?", "options": ["2πr", "πr²", "πd", "r²"], "answer": "πr²"},
                {"question": "The distance around a circle is?", "options": ["Area", "Circumference", "Diameter", "Radius"], "answer": "Circumference"},
                {"question": "Volume of a cube = ?", "options": ["l × b × h", "a³", "2a", "πr²h"], "answer": "a³"}
            ],
            "Statistics": [
                {"question": "Mean of 2, 4, 6, 8, 10?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "The middle value in data is?", "options": ["Mode", "Median", "Mean", "Range"], "answer": "Median"},
                {"question": "Most frequent number is?", "options": ["Mean", "Median", "Mode", "Range"], "answer": "Mode"},
                {"question": "Range = Highest – ?", "options": ["Lowest", "Median", "Mode", "Mean"], "answer": "Lowest"},
                {"question": "If mean = 20, total of 5 items = ?", "options": ["50", "60", "80", "100"], "answer": "100"}
            ]
        },
        "English": {
            "Literature": [
                {"question": "Who wrote 'Things Fall Apart'?", "options": ["Wole Soyinka", "Chinua Achebe", "Ngugi wa Thiong'o", "Amos Tutuola"], "answer": "Chinua Achebe"},
                {"question": "Poetry is written in?", "options": ["Prose", "Lines and stanzas", "Drama", "Essays"], "answer": "Lines and stanzas"},
                {"question": "A play is also called?", "options": ["Drama", "Novel", "Poem", "Essay"], "answer": "Drama"},
                {"question": "Author of 'The Lion and the Jewel'?", "options": ["Achebe", "Ngugi", "Soyinka", "Okigbo"], "answer": "Soyinka"},
                {"question": "The main character in a story is?", "options": ["Antagonist", "Protagonist", "Narrator", "Chorus"], "answer": "Protagonist"}
            ],
            "Grammar": [
                {"question": "Past tense of 'go' is?", "options": ["Gone", "Went", "Going", "Goes"], "answer": "Went"},
                {"question": "Choose the correct: She ___ to school yesterday.", "options": ["go", "goes", "went", "gone"], "answer": "went"},
                {"question": "Plural of 'child' is?", "options": ["Childs", "Children", "Childes", "Childrens"], "answer": "Children"},
                {"question": "Correct adjective form: He is ___ than me.", "options": ["tall", "taller", "tallest", "more tall"], "answer": "taller"},
                {"question": "Which is a conjunction?", "options": ["Run", "Beautiful", "And", "Quickly"], "answer": "And"}
            ],
            "Comprehension": [
                {"question": "Main idea of a passage is?", "options": ["Topic", "Summary", "Title", "Plot"], "answer": "Summary"},
                {"question": "To infer means?", "options": ["Guess without reason", "Conclude from evidence", "Copy directly", "Read aloud"], "answer": "Conclude from evidence"},
                {"question": "Skimming means?", "options": ["Reading carefully", "Reading quickly for main ideas", "Not reading at all", "Reading word for word"], "answer": "Reading quickly for main ideas"},
                {"question": "Scanning means?", "options": ["Looking for specific info", "Reading slowly", "Memorizing", "Explaining"], "answer": "Looking for specific info"},
                {"question": "Summary writing should be?", "options": ["Long", "Short and clear", "Confusing", "Copied"], "answer": "Short and clear"}
            ]
        },
        "Physics": {
            "Mechanics": [
                {"question": "Force = ?", "options": ["Mass × Distance", "Mass × Acceleration", "Work ÷ Time", "Power × Time"], "answer": "Mass × Acceleration"},
                {"question": "Unit of Force is?", "options": ["Joule", "Newton", "Pascal", "Watt"], "answer": "Newton"},
                {"question": "Speed = ?", "options": ["Distance ÷ Time", "Force ÷ Time", "Mass × Acceleration", "Work ÷ Power"], "answer": "Distance ÷ Time"},
                {"question": "Work = ?", "options": ["Force × Distance", "Power × Time", "Energy ÷ Time", "Mass × Acceleration"], "answer": "Force × Distance"},
                {"question": "1 horsepower = ?", "options": ["746 W", "1000 W", "1200 W", "500 W"], "answer": "746 W"}
            ],
            "Waves & Light": [
                {"question": "Light travels in?", "options": ["Curves", "Straight lines", "Circles", "Squares"], "answer": "Straight lines"},
                {"question": "Speed of light in vacuum?", "options": ["3.0 × 10⁸ m/s", "3.0 × 10⁶ m/s", "1.5 × 10⁸ m/s", "3.0 × 10⁴ m/s"], "answer": "3.0 × 10⁸ m/s"},
                {"question": "Convex lens is used for?", "options": ["Converging rays", "Diverging rays", "Blocking rays", "Diffusing light"], "answer": "Converging rays"},
                {"question": "Sound cannot travel through?", "options": ["Air", "Water", "Vacuum", "Steel"], "answer": "Vacuum"},
                {"question": "Rainbow is caused by?", "options": ["Reflection only", "Refraction and dispersion", "Diffraction only", "Absorption"], "answer": "Refraction and dispersion"}
            ],
            "Electricity": [
                {"question": "Unit of current is?", "options": ["Ampere", "Volt", "Ohm", "Coulomb"], "answer": "Ampere"},
                {"question": "V = IR is called?", "options": ["Hooke's law", "Ohm's law", "Newton's law", "Faraday's law"], "answer": "Ohm's law"},
                {"question": "Unit of resistance?", "options": ["Watt", "Ohm", "Volt", "Ampere"], "answer": "Ohm"},
                {"question": "Power = ?", "options": ["Work ÷ Time", "Force × Distance", "Mass × Acceleration", "Charge ÷ Time"], "answer": "Work ÷ Time"},
                {"question": "Fuse is used for?", "options": ["Protecting circuit", "Producing current", "Storing energy", "Reducing light"], "answer": "Protecting circuit"}
            ]
        },
        "Chemistry": {
            "Atomic Structure": [
                {"question": "Number of protons in atom is called?", "options": ["Mass number", "Atomic number", "Charge", "Isotope"], "answer": "Atomic number"},
                {"question": "Neutrons are found in?", "options": ["Nucleus", "Orbit", "Shell", "Outside atom"], "answer": "Nucleus"},
                {"question": "Isotopes have same ___ but different ___?", "options": ["Neutrons, Protons", "Protons, Neutrons", "Electrons, Protons", "Mass, Charge"], "answer": "Protons, Neutrons"},
                {"question": "Electron carries?", "options": ["Positive charge", "Negative charge", "Neutral", "Mass only"], "answer": "Negative charge"},
                {"question": "Relative mass of proton?", "options": ["0", "1", "2", "0.0005"], "answer": "1"}
            ],
            "Acids & Bases": [
                {"question": "Acid turns blue litmus?", "options": ["Red", "Green", "Yellow", "No change"], "answer": "Red"},
                {"question": "Base turns red litmus?", "options": ["Blue", "Green", "Yellow", "No change"], "answer": "Blue"},
                {"question": "pH scale runs from?", "options": ["1–7", "0–14", "1–10", "0–10"], "answer": "0–14"},
                {"question": "Neutral pH is?", "options": ["0", "7", "14", "10"], "answer": "7"},
                {"question": "Salt is formed from?", "options": ["Acid + Base", "Acid + Water", "Base + Oxygen", "Water + Hydrogen"], "answer": "Acid + Base"}
            ],
            "Organic Chemistry": [
                {"question": "Methane formula?", "options": ["CH₄", "C₂H₆", "C₃H₈", "C₄H₁₀"], "answer": "CH₄"},
                {"question": "Ethene is?", "options": ["Alkane", "Alkene", "Alkyne", "Alcohol"], "answer": "Alkene"},
                {"question": "C₂H₅OH is?", "options": ["Methane", "Ethanol", "Propane", "Ethanoic acid"], "answer": "Ethanol"},
                {"question": "General formula of alkanes?", "options": ["CnH2n", "CnH2n+2", "CnH2n–2", "CnHn"], "answer": "CnH2n+2"},
                {"question": "Petrol is mainly?", "options": ["Alkanes", "Alkenes", "Alcohols", "Acids"], "answer": "Alkanes"}
            ]
        },
        "Biology": {
            "Cell Biology": [
                {"question": "Basic unit of life is?", "options": ["Atom", "Tissue", "Cell", "Organ"], "answer": "Cell"},
                {"question": "Powerhouse of cell?", "options": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"], "answer": "Mitochondria"},
                {"question": "Plant cell has but animal cell lacks?", "options": ["Chloroplast", "Mitochondria", "Cytoplasm", "Nucleus"], "answer": "Chloroplast"},
                {"question": "Control center of cell is?", "options": ["Nucleus", "Cell wall", "Ribosome", "Cytoplasm"], "answer": "Nucleus"},
                {"question": "Protein synthesis occurs in?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], "answer": "Ribosome"}
            ],
            "Ecology": [
                {"question": "Group of same species living together?", "options": ["Community", "Population", "Ecosystem", "Habitat"], "answer": "Population"},
                {"question": "Study of living things and environment?", "options": ["Geography", "Ecology", "Biology", "Zoology"], "answer": "Ecology"},
                {"question": "Green plants are?", "options": ["Consumers", "Producers", "Decomposers", "Predators"], "answer": "Producers"},
                {"question": "Decomposers include?", "options": ["Bacteria and fungi", "Plants", "Animals", "Humans"], "answer": "Bacteria and fungi"},
                {"question": "Largest ecosystem is?", "options": ["Desert", "Ocean", "Forest", "Savanna"], "answer": "Ocean"}
            ],
            "Human Biology": [
                {"question": "Organ for pumping blood?", "options": ["Lungs", "Heart", "Kidney", "Liver"], "answer": "Heart"},
                {"question": "Organ for breathing?", "options": ["Liver", "Lungs", "Stomach", "Brain"], "answer": "Lungs"},
                {"question": "Excretory organ is?", "options": ["Kidney", "Liver", "Heart", "Lungs"], "answer": "Kidney"},
                {"question": "Brain is protected by?", "options": ["Ribs", "Skull", "Backbone", "Cartilage"], "answer": "Skull"},
                {"question": "Red blood cells carry?", "options": ["Oxygen", "Carbon dioxide", "Water", "Nutrients"], "answer": "Oxygen"}
            ]
        },
        "Government": {
            "Democracy": [
                {"question": "Democracy is defined as?", "options": ["Rule of one man", "Rule of the people", "Rule of the rich", "Rule of the soldiers"], "answer": "Rule of the people"},
                {"question": "Which is NOT a feature of democracy?", "options": ["Free elections", "Rule of law", "Dictatorship", "Fundamental rights"], "answer": "Dictatorship"},
                {"question": "Nigeria became a republic in?", "options": ["1960", "1963", "1979", "1999"], "answer": "1963"},
                {"question": "Head of government in parliamentary system?", "options": ["President", "Prime Minister", "Governor", "Speaker"], "answer": "Prime Minister"},
                {"question": "The 1999 Nigerian Constitution is?", "options": ["Unitary", "Confederal", "Federal", "Monarchical"], "answer": "Federal"}
            ],
            "Citizenship": [
                {"question": "A citizen is?", "options": ["Person with full rights in a state", "Foreigner", "Visitor", "Non-indigene"], "answer": "Person with full rights in a state"},
                {"question": "Method of acquiring citizenship NOT in Nigeria?", "options": ["Birth", "Naturalization", "Registration", "Colonization"], "answer": "Colonization"},
                {"question": "Loss of citizenship can be by?", "options": ["Renunciation", "Denunciation", "Deportation", "All of the above"], "answer": "All of the above"},
                {"question": "A citizen owes the state?", "options": ["Loyalty", "Taxes", "Obedience", "All of the above"], "answer": "All of the above"},
                {"question": "Dual citizenship is allowed in Nigeria?", "options": ["Yes", "No", "Sometimes", "Only for governors"], "answer": "Yes"}
            ],
            "Political Institutions": [
                {"question": "The legislature makes?", "options": ["Laws", "Money", "Judgments", "Policies"], "answer": "Laws"},
                {"question": "Judiciary interprets?", "options": ["Law", "Music", "Culture", "Economy"], "answer": "Law"},
                {"question": "Executive implements?", "options": ["Law", "Food", "Education", "Games"], "answer": "Law"},
                {"question": "Which is NOT an organ of government?", "options": ["Legislature", "Executive", "Judiciary", "Press"], "answer": "Press"},
                {"question": "Checks and balances means?", "options": ["Each organ controls others", "Only president rules", "No control", "Military rule"], "answer": "Each organ controls others"}
            ]
        },
        "Economics": {
            "Demand & Supply": [
                {"question": "Law of demand: As price rises, demand?", "options": ["Rises", "Falls", "Stable", "Doubles"], "answer": "Falls"},
                {"question": "Law of supply: As price rises, supply?", "options": ["Rises", "Falls", "Stable", "Zero"], "answer": "Rises"},
                {"question": "Intersection of demand & supply curve is?", "options": ["Equilibrium", "Surplus", "Shortage", "Inflation"], "answer": "Equilibrium"},
                {"question": "Excess supply leads to?", "options": ["Shortage", "Surplus", "Equilibrium", "Scarcity"], "answer": "Surplus"},
                {"question": "Excess demand leads to?", "options": ["Scarcity", "Shortage", "Surplus", "Inflation"], "answer": "Shortage"}
            ],
            "Money & Banking": [
                {"question": "Money serves as?", "options": ["Medium of exchange", "Store of value", "Unit of account", "All of the above"], "answer": "All of the above"},
                {"question": "Central Bank of Nigeria was founded in?", "options": ["1958", "1960", "1963", "1979"], "answer": "1958"},
                {"question": "Cheque is?", "options": ["Order to bank to pay", "Bank account", "ATM card", "Loan"], "answer": "Order to bank to pay"},
                {"question": "Commercial banks accept?", "options": ["Deposits", "Prayers", "Votes", "Citizenship"], "answer": "Deposits"},
                {"question": "ATM means?", "options": ["Automatic Teller Machine", "Account Transfer Method", "All Time Money", "Advanced Tax Mechanism"], "answer": "Automatic Teller Machine"}
            ],
            "National Income": [
                {"question": "GDP means?", "options": ["Gross Domestic Product", "Great Developed Product", "Gross Demand Price", "General Domestic Payment"], "answer": "Gross Domestic Product"},
                {"question": "GNP includes?", "options": ["Citizens abroad", "Only domestic goods", "Imports only", "Foreign debt"], "answer": "Citizens abroad"},
                {"question": "Per capita income = GDP ÷ ?", "options": ["Population", "Exports", "Imports", "Budget"], "answer": "Population"},
                {"question": "Inflation is?", "options": ["Rise in general price level", "Fall in prices", "Stability", "Zero growth"], "answer": "Rise in general price level"},
                {"question": "Unemployment means?", "options": ["No work for able people", "Retired people", "Children in school", "Tourists"], "answer": "No work for able people"}
            ]
        },
        "Literature": {
            "Prose": [
                {"question": "Prose is written in?", "options": ["Lines", "Paragraphs", "Verses", "Dialogues"], "answer": "Paragraphs"},
                {"question": "Author of 'Purple Hibiscus'?", "options": ["Chimamanda Ngozi Adichie", "Chinua Achebe", "Ngugi wa Thiong'o", "Wole Soyinka"], "answer": "Chimamanda Ngozi Adichie"},
                {"question": "Character opposing hero is?", "options": ["Protagonist", "Antagonist", "Narrator", "Author"], "answer": "Antagonist"},
                {"question": "Point of view in 'I walked home'?", "options": ["First person", "Second person", "Third person", "Omniscient"], "answer": "First person"},
                {"question": "Biography is story of?", "options": ["Animals", "Fiction", "Life of a person", "Imaginary events"], "answer": "Life of a person"}
            ],
            "Drama": [
                {"question": "Drama is written to be?", "options": ["Read silently", "Performed", "Printed only", "Sung"], "answer": "Performed"},
                {"question": "Stage directions guide?", "options": ["Actors", "Readers", "Writers", "Students"], "answer": "Actors"},
                {"question": "Comic relief means?", "options": ["Serious part", "Humorous break", "Tragedy", "Dialogue"], "answer": "Humorous break"},
                {"question": "Playwright means?", "options": ["Actor", "Writer of plays", "Dancer", "Poet"], "answer": "Writer of plays"},
                {"question": "Dialogue is between?", "options": ["Narrator", "Characters", "Audience", "Poet"], "answer": "Characters"}
            ],
            "Poetry": [
                {"question": "A line of poetry is called?", "options": ["Stanza", "Verse", "Paragraph", "Prose"], "answer": "Verse"},
                {"question": "14-line poem is called?", "options": ["Ode", "Sonnet", "Epic", "Elegy"], "answer": "Sonnet"},
                {"question": "Repetition of vowel sound is?", "options": ["Alliteration", "Assonance", "Rhyme", "Rhythm"], "answer": "Assonance"},
                {"question": "Narrative poem tells?", "options": ["A story", "A song", "A drama", "An essay"], "answer": "A story"},
                {"question": "Poem praising someone is?", "options": ["Ode", "Elegy", "Epic", "Sonnet"], "answer": "Ode"}
            ]
        },
        "CRS/IRS": {
            "Christian Religious Studies": [
                {"question": "Jesus was born in?", "options": ["Bethlehem", "Nazareth", "Jerusalem", "Rome"], "answer": "Bethlehem"},
                {"question": "Jesus fed 5000 with?", "options": ["5 loaves & 2 fish", "7 loaves", "Manna", "Corn"], "answer": "5 loaves & 2 fish"},
                {"question": "Baptism means?", "options": ["Immersion in water", "Running", "Fasting", "Sacrifice"], "answer": "Immersion in water"},
                {"question": "First miracle of Jesus?", "options": ["Walking on water", "Water to wine", "Healing blind", "Rising Lazarus"], "answer": "Water to wine"},
                {"question": "Jesus had how many disciples?", "options": ["10", "11", "12", "13"], "answer": "12"}
            ],
            "Islamic Religious Studies": [
                {"question": "Muslims face ___ during prayers?", "options": ["Kaaba", "Sun", "East", "Moon"], "answer": "Kaaba"},
                {"question": "Prophet Muhammad (SAW) was born in?", "options": ["Mecca", "Medina", "Jerusalem", "Baghdad"], "answer": "Mecca"},
                {"question": "Holy book of Islam is?", "options": ["Quran", "Bible", "Torah", "Injil"], "answer": "Quran"},
                {"question": "Fasting month is?", "options": ["Ramadan", "Muharram", "Eid", "Hajj"], "answer": "Ramadan"},
                {"question": "Number of daily prayers in Islam?", "options": ["3", "5", "7", "10"], "answer": "5"}
            ]
        }
    }
}

# Initialize session state variables
if 'current_class' not in st.session_state:
    st.session_state.current_class = None
if 'current_subject' not in st.session_state:
    st.session_state.current_subject = None
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = None
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# Function to start a new quiz
def start_quiz():
    st.session_state.quiz_questions = educational_content[
        st.session_state.current_class][st.session_state.current_subject][st.session_state.current_topic]
    random.shuffle(st.session_state.quiz_questions)
    st.session_state.current_question = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_completed = False
    st.session_state.score = 0
    st.session_state.start_time = datetime.now()

# Function to move to the next question
def next_question():
    if st.session_state.current_question < len(st.session_state.quiz_questions) - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.quiz_completed = True
        # Calculate score
        score = 0
        for i, question in enumerate(st.session_state.quiz_questions):
            if st.session_state.user_answers.get(i) == question['answer']:
                score += 1
        st.session_state.score = score

# Function to move to the previous question
def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

# Function to reset the quiz
def reset_quiz():
    st.session_state.current_class = None
    st.session_state.current_subject = None
    st.session_state.current_topic = None
    st.session_state.quiz_completed = False

# App title and sidebar
st.sidebar.title("EduQuiz 📚")
st.sidebar.markdown("### Select Your Class")
class_option = st.sidebar.selectbox(
    "Choose your class level:",
    list(educational_content.keys()),
    index=0 if not st.session_state.current_class else list(educational_content.keys()).index(st.session_state.current_class)
)

# Update current class if changed
if class_option != st.session_state.current_class:
    st.session_state.current_class = class_option
    st.session_state.current_subject = None
    st.session_state.current_topic = None

if st.session_state.current_class:
    st.sidebar.markdown("### Select Subject")
    subject_option = st.sidebar.selectbox(
        "Choose a subject:",
        list(educational_content[st.session_state.current_class].keys()),
        index=0 if not st.session_state.current_subject else list(educational_content[st.session_state.current_class].keys()).index(st.session_state.current_subject)
    )
    
    # Update current subject if changed
    if subject_option != st.session_state.current_subject:
        st.session_state.current_subject = subject_option
        st.session_state.current_topic = None
    
    if st.session_state.current_subject:
        st.sidebar.markdown("### Select Topic")
        topic_option = st.sidebar.selectbox(
            "Choose a topic:",
            list(educational_content[st.session_state.current_class][st.session_state.current_subject].keys()),
            index=0 if not st.session_state.current_topic else list(educational_content[st.session_state.current_class][st.session_state.current_subject].keys()).index(st.session_state.current_topic)
        )
        
        # Update current topic if changed
        if topic_option != st.session_state.current_topic:
            st.session_state.current_topic = topic_option
        
        # Start quiz button
        if st.sidebar.button("Start Quiz", use_container_width=True):
            start_quiz()

# Show quiz instructions
st.sidebar.markdown("---")
st.sidebar.info(
    "EduQuiz helps you prepare for exams with past questions from Primary 2 to SS3. "
    "Select your class, subject, and topic to start practicing!"
)

# Main app content
st.title("EduQuiz - Educational Quiz App")
st.markdown("### Test your knowledge with past questions from Primary 2 to SS3")

if not st.session_state.current_class:
    # Show class selection prompt
    st.info("Please select your class from the sidebar to begin.")
    
    # Display available classes
    cols = st.columns(len(educational_content))
    for i, (class_name, subjects) in enumerate(educational_content.items()):
        with cols[i]:
            st.subheader(class_name)
            for subject in subjects:
                st.write(f"- {subject}")
    
    # Display sample questions from different levels
    st.markdown("---")
    st.subheader("Sample Questions")
    
    sample_cols = st.columns(3)
    with sample_cols[0]:
        st.markdown("**Primary 2 Mathematics**")
        st.write("What is 5 + 3?")
        st.write("Options: 7, 8, 9, 10")
        st.success("Answer: 8")
    
    with sample_cols[1]:
        st.markdown("**JSS 2 Science**")
        st.write("Which organ pumps blood throughout the body?")
        st.write("Options: Liver, Heart, Lungs, Brain")
        st.success("Answer: Heart")
    
    with sample_cols[2]:
        st.markdown("**SSS 3 Physics**")
        st.write("What is the unit of electrical resistance?")
        st.write("Options: Volt, Ampere, Ohm, Watt")
        st.success("Answer: Ohm")

elif not st.session_state.quiz_questions:
    # Show subject and topic information
    st.header(f"{st.session_state.current_class} - {st.session_state.current_subject}")
    st.subheader(f"Topic: {st.session_state.current_topic}")
    
    # Display topic information and instructions
    st.info(f"Click 'Start Quiz' in the sidebar to begin the {st.session_state.current_topic} quiz.")
    
    # Show number of questions available
    num_questions = len(educational_content[st.session_state.current_class][st.session_state.current_subject][st.session_state.current_topic])
    st.write(f"Number of questions in this topic: {num_questions}")
    
    # Display sample question
    if num_questions > 0:
        sample_question = educational_content[st.session_state.current_class][st.session_state.current_subject][st.session_state.current_topic][0]
        st.markdown("**Sample Question:**")
        st.write(sample_question['question'])
        st.write("Options:", ", ".join(sample_question['options']))
        st.success(f"Answer: {sample_question['answer']}")

else:
    # Display quiz interface
    if not st.session_state.quiz_completed:
        # Show progress
        progress = st.session_state.current_question / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.caption(f"Question {st.session_state.current_question + 1} of {len(st.session_state.quiz_questions)}")
        
        # Display current question
        question_data = st.session_state.quiz_questions[st.session_state.current_question]
        
        st.header(f"Question {st.session_state.current_question + 1}")
        st.markdown(f"**{question_data['question']}**")
        
        # Store the user's answer
        user_answer = st.radio(
            "Select your answer:",
            question_data['options'],
            key=f"q{st.session_state.current_question}"
        )
        
        st.session_state.user_answers[st.session_state.current_question] = user_answer
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            if st.button("Previous") and st.session_state.current_question > 0:
                prev_question()
                st.rerun()
        with col2:
            if st.session_state.current_question < len(st.session_state.quiz_questions) - 1:
                if st.button("Next"):
                    next_question()
                    st.rerun()
            else:
                if st.button("Finish Quiz"):
                    next_question()
                    st.rerun()
        with col3:
            if st.button("Restart Quiz"):
                start_quiz()
                st.rerun()
    
    else:
        # Display quiz results
        st.header("Quiz Completed! 🎉")
        st.subheader(f"Your Score: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
        
        # Calculate percentage
        percentage = (st.session_state.score / len(st.session_state.quiz_questions)) * 100
        
        # Display performance message
        if percentage >= 80:
            st.success("Excellent! You have a great understanding of this topic!")
        elif percentage >= 60:
            st.warning("Good job! With a little more practice, you'll master this topic!")
        else:
            st.info("Keep studying! You'll improve with more practice.")
        
        # Show time taken
        if st.session_state.start_time:
            time_taken = datetime.now() - st.session_state.start_time
            st.write(f"Time taken: {time_taken.seconds // 60} minutes {time_taken.seconds % 60} seconds")
        
        # Display review of questions
        st.markdown("---")
        st.subheader("Review Questions")
        
        for i, question in enumerate(st.session_state.quiz_questions):
            expander = st.expander(f"Question {i+1}: {question['question']}")
            user_answer = st.session_state.user_answers.get(i, "Not answered")
            is_correct = user_answer == question['answer']
            
            expander.write(f"Your answer: {user_answer} {'✅' if is_correct else '❌'}")
            if not is_correct:
                expander.write(f"Correct answer: {question['answer']}")
        
        # Options after quiz completion
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Retry Same Quiz"):
                start_quiz()
                st.rerun()
        with col2:
            if st.button("Choose Different Topic"):
                reset_quiz()
                st.rerun()

# Footer
st.markdown("---")
st.caption("EduQuiz © 2023 | An educational quiz app with past questions from Primary 2 to SS3")