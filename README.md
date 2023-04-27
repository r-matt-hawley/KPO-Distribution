# KPO Music Distribution App
    To help KPO (Kingwood Pops Orchestra) distribute sheet music for the convenience of its members and for ease in following copyright laws (i.e, removing viewing permission after performance date).

---
## Rationale
After collecting music for a concert, scanners electronic copies to Google Drive where we control permissions for who can download music. Orhcestra members then download and print their respective parts according to their preferences (i.e, paper or tablet viewing). 

Not all orchestra members, however, have a gmail account. These members often have trouble "finding" music because gmail will not give them viewing access. Currently, we send these members unprotected pdf.

Additionally, interacting with Google Drive is different for every user, and dictating uniform instructions is not possible which causes confusion among orchestra members and scanning volunteers.

Ideally, this app will:
1. provide a uniform user experience where:
    - orchestra members can access sheet music for each concern and know whether they have each required piece of music,
    - scanners can distribute electronic copies of sheet music and control music access, and
    - administrators can plan concert set lists and communicate with the orchestra when music is ready for access;
2. mitigate litigation liability for KPO; and
3. serve as a localized database of concert music selection facilitating future concert planning. 

---
## User Groups
- Orhcestra Members who access music
- Scanners/Admin - might be separate groups
- Scanners add music according to parts (e.g, Trumpet I, Trumpet II, Flute I, Flute II, etc).
- Admins add, remove, and reassign orchestra members
- One person can hold multiple (or all) user groups
- Resource for implementing User groups: [Smashing Magazine](https://www.smashingmagazine.com/2020/02/django-highlights-user-models-authentication/)

---

## Requirements
- User roles should be easily transferrable, i.e, when the appropriate board members rotate on/off the board, their priviledges can be added or removed as appropriate
- Sheet music is stored by instrument part so that an orchestra member can view/print music or export to external application.
- Members should be able to view music of any part, but they can download only their own parts
- After each concert all permissions to view, etc. should be discontinued. 
- Users can view what pieces have been released by concert
    - Scanners view:
        - what pieces have been uploaded (Did we miss a part?)
        - what parts have been uploaded to each piece (Does this piece have English horn? What pieces have piccolo?)
    - Orchestra members view:
        - what pieces have "come in" from the rental companies
- Non programmers can manage the structure of the application within the scope of these requirements.

---
## Web Pages by User Role

### **All Users**
#### Login

#### Sign Up
- New Users must be approved by Administrators to be able to interact with the application (see [Registration](#registration))

##### *Registration*
- KPO Board compiles list of members' emails
- Once a member registers an account, their email is matched to the list, and their user role and/or orchestra section is assigned.
    - If a registrant's email does not match the member list, the application alerts admins via email
    - Admin should add new orchestra members to the member list before the member's first rehearsal.
    - TODO: Do we need to distribute music to ringers? 

#### Profile Page
- Lists User permissions, part assignments
- Change Password

### **Orchestra Members**
#### View Set List
- Songs are sorted by modified timestamp, title, or performance order.
- Orchestra members view songs that Scanners have uploaded.
- So that Orchestra Members know what music has not yet "come in," songs that have no pdf files appear separate from songs that have music uploaded.
- Clicking a song title renders an HTML view of the song.
- Members may select any combination of songs to create a single file to print or download.
- Members may select any combination of songs to print or download all chosen files separately.
- Once the concert date passes, all viewing permissions are provoked.

#### Music Download
- If the Member has permission to download music, a download/print button will appear.
- If the Member has only view permission, no download/print button appears, but a message affirming read only permission appears instead.

### **Scanners**
#### View Set List
- Same as [Orchestra Members](#view-set-list)

#### Add Music
- Scanners upload files (TODO: Does the app require a certain format?) and specify song title and part name.
- Scanners select part name via clicking icons or search bar.
- Selections remain after uploading file. (Include a clear button.)
- List parts with previously uploaded music.


### **Administrators**
#### View Parts
- Displays a colored matrix showing what parts have (not) been uploaded for each song.
- Songs in matrix link to [View Set List](#view-set-list)
- View previous concerts

#### Manage Concerts
- Administrators can insert new songs, categorize songs (full orchestra, brass only, strings only), specify performance order, specify concert date (automatically removes viewing permission).

#### Manage Users
- Administrators view, add, or remove Orchestra Members (organized by part), Scanners, or other Administrators

---
## Data
Need to store:
- Music
    - Song Title
    - Part name
    - File
    - Created timestamp
    - Modified timestamp
- Concert
    - Title
    - Performance Date
    - Season
        - Fall
        - Christmas
        - February
        - Spring
- Django Stores Users automatically with `django.contrib.auth`

### [Tables](https://dbdiagram.io/d/643efa826b31947051d04564)
![Entity-Relationship Diagram](./images/KPO%20Distribution.png)

---
## Brainstorm
- PDF expires after concert date
- Orchestra members can select songs to print. Then, the app creates a single pdf file for members to print all pages at once.
- App flags when members download music so that admin can see which sections of the orchestra have downloaded each piece. This might help admin catch if a given section is missing music before the first rehearsal.
- Members may view 2 or more parts or songs side by side.
- Include roster of orchestra by section.
- Pre-Interview: All songs are deleted after the performance date. Post-Interview, memb
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/)
- Admin toggles `is_published` to all view permissions for music from scanners to orchestra memebers.
- Need notes fields for Concert, Song, and Part tables.
- Use [Model Manager](https://docs.djangoproject.com/en/4.2/topics/db/managers/#modifying-a-manager-s-initial-queryset) to return all songs for the upcoming concert
- When uploading a music file, the form should automatically create the file name from the data that the Scanners provide.