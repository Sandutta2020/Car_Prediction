function form_validate() {    
    year =document.myForm.Year.value;
    var text = /^[0-9]+$/;
    if (year != 0) {
        if ((year != "") && (!text.test(year))) {

            alert("Please Enter Numeric Values Only");
            return false;
        }
    }
    if (year.length != 4) {
        alert("Year is not proper. Please check");
        return false;
        }
    var current_year=new Date().getFullYear();
    if((year < 1920) || (year > current_year))
    {
    alert("Year should be in range 1920 to current year");
    return false;
    }

    return true;
   
}