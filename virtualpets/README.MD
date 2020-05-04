<h1>Virtual Pets</h1>

*Check it out <a href="http://ulam10.pythonanywhere.com/">here!</a>
*Due to deployment issues, PostgreSQL is not available, and I'm currently looking into a workaround. Updated functional app link coming soon!

Virtual Pets is a virtual pet simulation game. Adopt a wild animal or create your own. Set a feeding schedule for your pets, or add them to a virtual playground to get some exercise while playing with other pets.

<h3>Technologies Used</h3>
    <lu>
        <li>Django</li>
        <li>Python</li>
        <li>PostgreSQL</li>
        <li>HTML5</li>
        <li>CSS</li>
        <li>Bootstrap</li>
        <li>jQuery</li>
        <li>JSON</li>
    </lu>

<h3>Existing Features</h3>
    <lu>
        <li>CRUD on Users and pets</li>
        <li>User Authentication</li>
        <li>Data Validation and Error Handling</li>
        <li>Responsive Design</li>
        <li>User can switch their pets to different playgrounds</li>
        <li>Profile view</li>
        <li>Playground page</li>
        <li>Admins can add Playgrounds(pg_create)</li>
        <li>Admins can remove Playgrounds(pg_delete)</li>
        <li>Edit Playground features(pg_update)</li>
        <li>Extended Models and Relationships</li>
        <li>CSS Animation</li>
    </lu>

<h3>Planned Features</h3>
    <lu>
        <li>Pet age timer and life cycle</li>
        <li>User store for pet accessories</li>
        <li>Ability for the user to remove their pet in the playground_detail page </li>
        <li>Ability to release pet into the wild for other users to adopt</li>
        <li>Specific time to serve the meals</li>
        <li>Playground-image where pets can be added</li>
        <li>Upload images and set requirements</li>
        <li>Add images to profile, playgrounds,pets </li>
        <li>Add Google Map to playgrounds</li>
        <li>Pet trading between users</li>
    </lu>
    
<h3>User Story</h3>
Upon landing on the home page, a user can sign up with his/her name and email address. 
Users can use his/her credentials to log in.

Once logged in, user can:
View profile (user detail), 
Edit profile. Add more info (i.e., first name, last name) to profile (user update)
Delete profile (user delete)


PETS - User can also:
View all available virtual pets (pet index), 
Add their own pet to the list (pet create), 
Select a pet they want to play with (association). A user can have many pets.
Update pet info (pet update)

<h3>Wireframes</h3>
<img src="virtualpets/main_app/static/images/home.png">
<img src="virtualpets/main_app/static/images/about.png">
<img src="virtualpets/main_app/static/images/petindex.png">
<img src="virtualpets/main_app/static/images/petdetails.png">
<img src="virtualpets/main_app/static/images/pgindex.png">
<img src="virtualpets/main_app/static/images/pgdetails.png">

<h3>Data Model</h3>
<img src="virtualpets/main_app/static/images/model.png">

<h3> Milestones</h3>
    <lu>
        <li>Getting user Auth to work</li>
        <li>Remove toy associations since the project was based off lab/homework</li>
        <li>Playground model/view/templates. Decided to not go full CRUD</li>
        <li>Added concept of wild pets, pets that have no owners. Figured out how to display them for non*logged in users</li>
        <li>Got forms working for user edit and pet creation/edits</li>
        <li>Materialize stripped out, replaced with Bootstrap</li>
        <li>Created home/about pages</li>
    <li>Fixed not letting pets be part of multiple playgrounds, their owner must remove them from a playrgound before placing them in another.</li>
        <li>Added full CRUD for User.</li>
        <li>Added ability to let wild pets become adopted</li>
    </lu>

<h3>Delegation</h3>

We let everyone pick what they wanted to work on so Eddie ended up tackling most of the styling and Uyen and Steven focused mostly on backend parts of the project. There was some overlap and paired programming so everyone got to see and work on both frond and back end
