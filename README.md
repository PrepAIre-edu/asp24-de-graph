# Граф концептів — силабуси KSE (4 курси)

Один граф на всі чотири силабуси з `Syllabuses/`. Замінює `_linear_algebra/` — Linear Algebra тут той самий, плюс три нові курси й міжпредметні зв'язки. Стару теку можна видалити.

## Числа

| | до (лише LA) | **тепер** |
|---|---|---|
| курси | 1 | **4** |
| юніти | 15 | **51** |
| концепти | 29 | **144** |
| зв'язки | 64 | **254** |
| міжпредметні зв'язки | 0 | **38** |
| входження з цитатами | 70 | **193** |

| | |
|---|---|
| цитати верифіковані дослівно | **193 / 193 = 100 %** |
| компоненти зв'язності | 1 — граф суцільний |
| prerequisite | ациклічний; усі 144 концепти в одному порядку вивчення |
| типи зв'язків | prerequisite 185, applies_to 23, related 22, contrasts_with 13, part_of 11 |

### По курсах

| курс | джерело | юніти | концепти |
|---|---|---|---|
| **CALC** — Calculus | 15 лекцій у 4 темах (Limits, Derivatives, Integral, Series) | 15 | 43 |
| **PROB** — Probability Essentials | 16 «Preparation lecture materials» у 5 блоках | 15 | 29 |
| **ML** — Machine Learning | 6 модулів; теми задані маркованими списками | 6 | 43 |
| **LA** — Linear Algebra Basics | 15 практичних сесій за 7 тижнів | 15 | 29 |

## Файли

- **`dataset/concept_graph.html`** — інтерактивний граф. Фільтр «лише міжкурсові» тут уперше має сенс: показує 38 ребер, що зшивають чотири курси.
- **`dataset/concept_graph.json`** — усе одним файлом.
- `dataset/*.csv` — concepts, concept_links, concept_occurrences, units (з назвами лекцій), modules, courses, source_files.
- `dataset/seed_concepts.sql` — під ту саму `_concept_graph/db/schema.sql`.
- `build/src_calc.py`, `src_prob.py`, `src_ml.py`, `src_links.py` — джерело істини в читабельному вигляді. LA переюзаний із `_linear_algebra/build/extractions_src.py`, не переписаний.
- `build/quality_report.json` — повний звіт.

## Найцінніше: 38 міжпредметних зв'язків

Це те, чого не було, поки курси жили окремо. Розподіл:

| напрям | ребер |
|---|---|
| LA → ML | 12 |
| PROB → ML | 10 |
| CALC → ML | 5 |
| CALC → PROB | 4 |
| решта (ML → PROB, ML → CALC, PROB → LA, LA → PROB, ML → LA) | 7 |

Ключові ланцюги, які тепер граф знає:

- `derivative` + `differentiation-rules` (CALC) → **`backpropagation`** (ML). Backprop — це буквально ланцюгове правило, застосоване до мережі.
- `matrix-vector-multiplication` (LA) → **`artificial-neuron`**; `matrix-multiplication` → `feedforward-network`. Зважена сума нейрона — це скалярний добуток, шар — множення на матрицю.
- `matrix` + `linear-space` (LA) → **`pca`**. PCA — власний розклад коваріаційної матриці.
- `system-of-linear-equations` + `solving-sle-with-inverse` (LA) → **`linear-regression`**. Нормальні рівняння — це СЛАР.
- `set` → `event-space` → `probability` → `conditional-probability` → `bayes-rule` (PROB) → **`classification`** (ML).
- `expected-value` (PROB) → `averaging-and-voting`, `variance` → **`bagging`**. Беггінг — прямий засіб зниження дисперсії.
- `series` + `convergence-of-series` (CALC) → **`expected-value`** (PROB). Дискретне сподівання — це ряд, і він мусить сходитися.

Перевірив явно, що порядок тримається: `derivative` (#53) раніше за `backpropagation` (#140), `matrix` (#7) раніше за `pca`, `set` (#10) раніше за `bayes-rule`.

## Порядок вивчення, що виходить із графа

Топологічне сортування prerequisite-підграфа охоплює **всі 144 концепти** й має рівно **шість коренів** — і це саме ті шість, які мають бути справжніми початковими точками:

```
set · sequence · matrix · vector · linear-equation · logical-proposition
```

Завершується граф на `deep-learning`, `training-loop`, `convolution-operation`, `backpropagation`, `holistic-evaluation` — тобто найглибшому матеріалі ML, який спирається на всі три математичні курси. Це і є той запит, який виконуватиме агент-генератор.

## Дві речі, які виявила валідація

**1. Та сама пастка з типами зв'язків, що й у LA — і вона повторювана.** Після першого прогону 13 концептів виявилися коренями prerequisite-підграфа. Шість справжні, а сім — артефакти: `decision-tree` мав лише `applies_to:classification`, `ensemble-learning` — нічого, `little-o-notation` — лише `contrasts_with:big-o-notation`, `baseline` — лише `related:accuracy`. Тобто **`applies_to`, `contrasts_with` і `related` не несуть інформації про порядок**, і якщо покладатися лише на них, порядок уроків виходить безглуздим. Додав 8 явних `prerequisite`.

Це вже другий раз, коли та сама помилка з'явилася на новому матеріалі. Для агента це означає конкретну перевірку, яку варто додати в `validate.py`: **порахувати корені prerequisite-підграфа й попередити, якщо їх більше, ніж очікувана кількість фундаментальних понять, або якщо в кореня складність ≥ 3**. `curse-of-dimensionality` (d4) як корінь — очевидний сигнал помилки; `set` (d1) — ні.

**2. Префільтр злиття дав 6 кандидатів, і всі шість — правильно відхилені.** `supervised-learning`/`unsupervised-learning`, `definite-integral`/`indefinite-integral`, `l1-regularization`/`l2-regularization`, `differentiable-function`/`differential`. Лексична схожість назв тут висока (0.90–0.96), але це протилежності або варіанти, а не дублікати. Добра ілюстрація, чому R1 — це LLM-арбітраж, а не автоматичне злиття за порогом: злиття «за схожістю назви» зруйнувало б граф саме в цих місцях.

## Обмеження

- **Визначення написані мною.** У силабусах їх немає — є лише назви тем. Цитати доказують, що тему заплановано, і нічого більше. Це головна причина не заливати цей граф у продакшн як фінальний: коли з'являться реальні матеріали (лекції, конспекти), визначення треба перезібрати з них, а цей граф лишити скелетом і планом.
- **Concepts/unit 1–9, а не 5–10.** Гейт запускався з `min_concepts_per_unit=1`. Для рядка таблиці в силабусі вимагати п'ять понять означало б їх вигадати. Медіана — 3.
- **Немає зв'язків із графом MIT.** Ти не просив, і я не робив. Місця зшивання очевидні й тепер їх більше, ніж було з одним LA: `supervised-learning`, `deep-learning`, `pca`, `precision`/`recall` тут ↔ однойменні концепти в MIT AI/DBS. Це буде не додавання ребер, а **справжнє злиття вузлів** — у графі MIT уже є `supervised-learning`, `machine-learning`, `precision`, `recall`, `clustering`. Тобто це задача для `find_merges`, а не лише `find_bridges`, і робити її варто свідомо: два графи описують те саме різними словами й різної глибини.
- **ML → CALC і ML → PROB (3 ребра) виглядають як зворотний напрям.** Це `training-loop → convexity` тощо, де я моделював «метод спирається на теорію», а не календарний порядок. Вони не порушують DAG, але якщо тебе цікавить строго напрям «математика перед застосуванням», ці три варто передивитися.
