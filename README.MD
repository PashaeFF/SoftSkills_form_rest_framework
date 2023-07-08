# Create Soft Skill Forms (API)
- [Create your soft skill forms](#create-soft-skill-forms)
- [Project Title](#project-title)
- [Description](#description)
    - [Azərbaycanca](#az)
    - [English](#en)

<hr>

- İnstallation/Quraşdırılma
- [İnstallation](#installation)
- [Author](#author)
- [Version](#version)
___



<hr>

# Project Title
___
* <b>Create your soft skill forms</b>
___

# Description

## AZ
___
* <b>Skript Django RestFramework.</b>
* <b>Forma dinamikdir.</b>
* <b>50 suallıq sorğu formu yaratmaq mümkündür.</b>
    1. 10 sual listi.
    2. Hər listin içərisində 5 sual.
    3. Hər sualın tərkibində 1 sual, 4 cavab variantı və hər cavab variantı üçün bal sistemi var.
    4. Ballar hər sual listinə uyğun olaraq toplanıb hesablanır. Məsələn: <br/>
        4.1. <code>question_list_1 = {'point': 5}</code>
    <br/>
* <b>Formada icazələr əlavə olunub, yalnız "Superuser" forma yarada bilir.</b>
* <b>Hər istifadəçinin doldurduğu formaya hər kəs baxa bilər, lakin hər istifadəçi balları görə bilmir. Yalnız "company" və "superuser" icazəsi olan şəxslər balları görə bilir. Formanı dolduran şəxs də balları görə bilmir, ümumiyyətlə orada bal olduğundan xəbəri olmur. Səbəb isə Kompaniyaların özlərinə uyğun olan şəxslərin seçə bilməsidir.</b>
____


## EN
___
* <b>The script is built with Django RestFramework.</b>
* <b>Form is dynamic.</b>
* <b>It is possible to create a questionnaire consisting of 50 questions.</b>
    1. A list of 10 questions.
    2. 5 questions in each list.
    3. Each question has 1 question, 4 answer options and a point system for each answer option.
    4. Points are collected and calculated according to each list of questions. For example: <br/>
        4.1. <code>question_list_1 = {'point': 5}</code>
    <br/>
* <b>Permissions have been added to the form, only "Superuser" can create the form.</b>
* <b>Every user can see the form filled by every user, but not every user can see the scores. Only people with "company" and "superuser" permission can see the scores. The person filling out the form also cannot see the points and usually does not know that there are points. The reason is that companies can choose the right people for them.</b>
____

# Installation

<code>python3 -m venv <venv\> </code><br/>
<code>source <venv\>/bin/activate</code> (MacOS/Linux)<br/>
<code><venv\>/Scripts/activate</code> (Windows)<br/> 
<code>pip install -r requirements.txt</code><br/>
<code>python manage.py runserver</code><br/> 

____

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

# Version

>* <b>v1.0</b>
>* <b>Initial Release</b>

___