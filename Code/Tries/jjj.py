from json import dump

data = {"знать": ['ХХ Всероссийская научная конференция ИТСАУ-2022', 
                  'Урок НТИ', 
                  'Образовательный цикл ПТК.',
                  'Лекция на тему: "Регистрация программ для ЭВМ и баз данных"',
                  'Воркшоп сессия "Будь первым"',
                  'СТАРТАПЫ LETI — Закрытая питч-сессия проектов. Поток 1',
                  'Нейминг: этапы и способы создания #SBS',
                  'Экспертиза по запросу для для команд Акселератора "Стартап-полигон"',
                  'Лекция по работе с институтами развития и источниками финансирования стартапов',
                  'Акселерационная программа "Тайга.АгроБиоФармТехнологии". Вебинар 31. Основы изобретательской деятельности.',
                  'Выставка достижений беспилотной авиации',
                  'Выставка беспилотников',
                  'Лекция Станислава Дробышевского "Кроманьонцы"',
                  'Лекторий ЭкоШколы. Лекция 3 "Почему горят наши леса и что с этим делать?"',
                  'Лекция + практикум «Марк Аврелий: Как работать над собой? + учимся вести дневник»',
                  'Лекция «Витражист Гарри Кларк – гений «с темной стороны Луны»',
                  'Лекция «Материалы и технологии производства ювелирных изделий»',
                  'Бесплатная экскурсия в Институт медико-биологических проблем РАН',
                  'Международная творческая выставке «Диалог 10»',
                  'Конференция, посвященная памяти советского архитектора',
                  'Выставка «О том, что близко»',
                  'Всероссийском фестивале дизайна',
                  'XLIX Международная научно-практическая конференция «Advances in Science and Technology»',
                  'Международная научно-практическая конференция «Eurasiascience»',
                  'Международная научно-практическая конференция «Концепция «общества знаний» в современной науке'
                  'Акселератор в сфере онлайн продаж',
                  'Акселератор сферы развлечений и организации досуга',
                  'Акселератор в сфере ресторанов и общественного питания',
                  'Акселератор ФРИИ',
                  'Онлайн-семинар "Сердечно-сосудистые осложнения некардиальных хирургических операций: обзор современных клинических рекомендаций"',
                  'Вебинар "Синдром подмышечной лимфоаденопатии" в рамках научно-образовательного проекта РОО "СПРО".'
                  'Географический диктант',
                  'VI городская научно-практическая конференция «Социально-культурное проектирование в городе Москве: ведущие тенденции и актуальные практики»',
                  'Национальная научно-практическая конференция «Стратегические приоритеты развития сферы закупок»',
                  'Национальная (всероссийская) научно-практическая конференция с международным участием «Технологии, модели и алгоритмы модернизации науки в современных геополитических условиях»',
                  'XLIX Международная научно-практическая конференция "Advances in Science and Technology".',
                  'XXVIII Международная научно-практическая конференция "Современная наука: актуальные вопросы, достижения и инновации"',
                  'Международная научно-практическая конференция "Новый путь российской экономики: импортозамещение, инновационность, экономическая безопасность"',
                  'Выставка Лучших Выпускников Дизайнеров ОТЛИЧНО 2022',
                  'Научная конференция «БУДЬ В РЕСУРСЕ»',
                  'Конференция "Водородная промышленность на Северо-Востоке России"',
                  'IV сессия "Школы энергетики ВТИ"',
                  'Стратегическая сессия «Поиск подходов к развитию программы «Высокозатратные нозологии»',
                  'День открытых дверей на медицинском факультете',
                  'Научно-популярная лекция «Как была решена самая знаменитая математическая задача XX века»',
                  ],
        
        "уметь": ['Трек 3 (Работа со стартапами со стороны корпораций)',
                  'Трекшн-сессия № 8 "Выход из зоны комфорта. Определение точек роста". Трекер Коробкина. Команда № 3',
                  'Трекшн-сессия № 5 «Выход из зоны комфорта. Определение точек роста» Чешева М.Ф. Команда № 4,5',
                  'Мастер-класс по подготовке к питчу и созданию итоговой презентации',
                  'Трекшн-митинг для команд Акселератора «Стартап-полигон»',
                  'Презентация дальнейших вариантов развития студенческих технологических проектов "EcoNet Challenge" ТюмГУ',
                  'Курс «Формирование новых когнитивных инструментов»',
                  'Международная проектная школа',
                  'Комплексный курс для начинающих сметчиков',
                  'Лекция + практикум «Марк Аврелий: Как работать над собой? + учимся вести дневник»',
                  'Скульптурный курс «Анатомия портрета»',
                  'Совместный просмотр Avito Analytics meetup #8 в офисе Авито',
                  'Бесплатный вебинар: Битрикс24 — как не провалить внедрение CRM?',
                  'Вебинар "Современные тенденции радиотерапии опухолей желудочно-кишечного тракта" в рамках научно-образовательного проекта РОО "СПРО"',
                  'Курс "Продвинутый пользователь Word"',
                  'Курс "Текстовый редактор Google Документы"',
                  'Форум молодых лидеров «Россия – Центрально-Азиатский регион»',
                  'Евразийский технологический форум',
                  'Учебные сборы',
                  'Международный научный форум «FIT-M 2022»',
                  'Авторский лекционно-практический курс "Диагностика заболеваний слизистой оболочки полости рта"',
                  'Симуляционный мастер-класс "Безопасная техника инъекций "'
                  'Курс "Веб-разработчик с нуля"',
                  'Питч-сессии стартапов с партнерами акселерационной программы',
                  'Регулярная встреча №117 бизнес - клуба публичных выступлений Optima Forma',
                  'Стратегическая сессия "Развитие социальных лифтов в России"',
                  'Школа Предпринимателей Основа #партнеры',
                  'Школа добровольных лесных пожарных. Вводное занятие',
                  'Школа SEO #партнеры',
                  '«Зимняя IT-школа» в Томском политехе',
                  'Школа Предпринимателей Основа #партнеры',
                  'Онлайн-мастер-класс «Перспективы и возможности создания цифровой криптоэкономики в РФ»'
                  ],
        
        "владеть": ['Встреча команды "Метафест" с трекером',
                    'Олимпиада «Покори Воробьевы горы!»'
                    'Встреча команды "ЛиТрип" с трекером',
                    'Защита стартап проектов Акселератора #МореИдей (Поток №2)',
                    'Демо-день #Забава',
                    'Труба экспертов',
                    "Практический курс по всем дефектам фронтальных зубов",
                    'Проектная работа команды СамГМУ',
                    'Демо-день 1 "Лучший студенческий стартап"',
                    'Акселератор ИнноВектор. Экспертиза стартап-проектов',
                    'Демо-день для проектов-выпускников. Гиппократ с нами',
                    'Дискуссия «Познание vs здравый смысл: ученый здорового человека»',
                    'Технологический диктант',
                    'Московская традиционная олимпиада по лингвистике',
                    'Суперфинал Национальной технологической олимпиады',
                    'Творческий нетворкинг',
                    'Конкурс технических решений «Hi-Fly»',
                    'Всероссийская олимпиада по математике',
                    'Лидерская сессия «СтудПлюс»',
                    'Региональный чемпионат по искусственному интеллекту',
                    'Предпринимательский турнир',
                    'Реализация пилотных проектов: юридические нюансы взаимодейтсвия с бизнес и гос. заказчиками',
                    'Олимпиада «Будущие исследователи – будущее науки»',
                    'Московская олимпиада по финансовой грамотности',
                    'Олимпиада школьников «Физтех» по математике',
                    'Турнир городов',
                    'Московская олимпиада по географии',
                    'Объединенная межвузовская математическая олимпиада',
                    'Всероссийская олимпиада по информатике',
                    'Всероссийская олимпиада по ОБЖ',
                    'Всероссийская олимпиада по физике',
                    'Всероссийская олимпиада по литературе'
                    'Квалификационный турнир',
                    'конкурс «УМНИК»',
                    'Турнир математических боев им. А. П. Савина',
                    'Олимпиада «Максвелл»',
                    'МОСКОВСКАЯ КОМАНДНАЯ ОЛИМПИАДА', 
                    'Диктант по энергосбережению',
                    'Технологический диктант',
                    'Тютчевский диктант',
                    'Казачий диктант – 2022',
                    'Всероссийский диктант по английскому языку',
                    'Антикоррупционный диктант 2022',
                    '«Московская Ярмарка Стартапов»',
                    'Прямой эфир III Международной обучающей математической олимпиады. Олимпиада для влюблённых в математику',
                    'Встреча открытого клуба предпринимателей "БИЗНЕС-ДРАЙВ"',
                    'Новый отбор в акселератор Спринт',
                    'Всероссийский конкурс молодежных проектов "Воплоти свою мечту!"',
                    ]
        }

with open("data.json", "w") as fp:
    dump(data,fp) 