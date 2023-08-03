function toggleCollapse(){
    let navbar = document.getElementById("navbar")
    let heading = document.getElementById("navbar-heading")
    let headingTags = document.querySelectorAll("h4")
    let headerNavDiv = document.getElementById("header-nav-div")
    let welcome = document.getElementById("user-welcome")
    let container = document.getElementById("container")
    let searchInput = document.getElementById("search")
    let logoutBtn = document.getElementById("logout-btn")

    navbar.classList.toggle("active")

    if (navbar.classList.contains("active")){
        heading.style.display = 'none';
        headerNavDiv.style.justifyContent = "center"
        headingTags.forEach((heading) => {
            heading.style.display = "none";
        });
        welcome.style.display = 'none';
        container.style.width = 'calc(100% - 77px)';
        container.style.marginLeft = '92px';
        searchInput.style.display = 'none';
        logoutBtn.style.display = 'none';

    }else{
        heading.style.display = 'flex';
        headerNavDiv.style.justifyContent = "space-between";
        headingTags.forEach((heading) => {
            heading.style.display = "block";
        });
        welcome.style.display = 'block';
        container.style.width = 'calc(100% - 290px)';
        container.style.marginLeft = '290px';
        searchInput.style.display = 'flex';
        logoutBtn.style.display = 'block';


    }
}

const toggleFilterMenu = () => {
    const filterMenu = document.querySelector(".filter-menu");
    filterMenu.classList.toggle("active-filter-menu")
}