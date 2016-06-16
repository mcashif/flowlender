var locations = [
    ['NEWYORK', "KIDS", "November 16", 48.87, 2.29, "/index-detail", "assets/img/properties/property-01.jpg", "/static/assets/img/property-types/apartment.png"],
    ['CHICAGO', "KIDS", "November 16. 2016", 48.866876, 2.309639, "/index-detail", "assets/img/properties/property-02.jpg", "/static/assets/img/property-types/apartment.png"],

    ['NEWYORK', "KIDS", "December 16. 2019", 48.874796, 2.299275, "/index-detail", "assets/img/properties/property-03.jpg", "/static/assets/img/property-types/construction-site.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.864194, 2.288868, "/index-detail", "assets/img/properties/property-04.jpg", "/static/assets/img/property-types/cottage.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.881187, 2.276938, "/index-detail", "assets/img/properties/property-06.jpg", "/static/assets/img/property-types/garage.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.859098, 2.423515, "/index-detail", "assets/img/properties/property-08.jpg", "/static/assets/img/property-types/houseboat.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.872296, 2.287796, "/index-detail", "assets/img/properties/property-07.jpg", "/static/assets/img/property-types/land.png"],

    ['NEWYORK', "KIDS", "December 16. 2019", 48.874457, 2.254386, "/index-detail", "assets/img/properties/property-09.jpg", "/static/assets/img/property-types/single-family.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.875191, 2.252412, "/index-detail", "assets/img/properties/property-10.jpg", "/static/assets/img/property-types/villa.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.864352, 2.257218, "/index-detail", "assets/img/properties/property-11.jpg", "/static/assets/img/property-types/vineyard.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.858648, 2.273526, "/index-detail", "assets/img/properties/property-12.jpg", "/static/assets/img/property-types/warehouse.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.856277, 2.264256, "/index-detail", "assets/img/properties/property-13.jpg", "/static/assets/img/property-types/industrial-site.png"],

    ['NEWYORK', "KIDS", "December 16. 2019", 48.859988, 2.252991, "/index-detail", "assets/img/properties/property-01.jpg", "/static/assets/img/property-types/apartment.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.856954, 2.283912, "/index-detail", "assets/img/properties/property-05.jpg", "/static/assets/img/property-types/condominium.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.879268, 2.270672, "/index-detail", "assets/img/properties/property-06.jpg", "/static/assets/img/property-types/construction-site.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.875925, 2.3239098, "/index-detail", "assets/img/properties/property-03.jpg", "/static/assets/img/property-types/cottage.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.870393, 2.327771, "/index-detail", "assets/img/properties/property-04.jpg", "/static/assets/img/property-types/houseboat.png"],

    ['NEWYORK', "KIDS", "December 16. 2019", 48.880328, 2.307258, "/index-detail", "assets/img/properties/property-08.jpg", "/static/assets/img/property-types/land.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.880284, 2.306721, "/index-detail", "assets/img/properties/property-09.jpg", "/static/assets/img/property-types/single-family.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.860342, 2.304597, "/index-detail", "assets/img/properties/property-10.jpg", "/static/assets/img/property-types/vineyard.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.852549, 2.329574, "/index-detail", "assets/img/properties/property-11.jpg", "/static/assets/img/property-types/warehouse.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.857124, 2.316699, "/index-detail", "assets/img/properties/property-12.jpg", "/static/assets/img/property-types/empty.png"],

    ['NEWYORK', "KIDS", "December 16. 2019", 48.869433, 2.315068, "/index-detail", "assets/img/properties/property-13.jpg", "/static/assets/img/property-types/apartment.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.885916, 2.297130, "/index-detail", "assets/img/properties/property-01.jpg", "/static/assets/img/property-types/industrial-site.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.893534, 2.276616, "/index-detail", "assets/img/properties/property-02.jpg", "/static/assets/img/property-types/construction-site.png"],
    ['CHICAGO', "ADULTS", "November 16. 2016", 48.872570, 2.237349, "/index-detail", "assets/img/properties/property-03.jpg", "/static/assets/img/property-types/cottage.png"],
    ['NEWYORK', "KIDS", "December 16. 2019", 48.879344, 2.226191, "/index-detail", "assets/img/properties/property-04.jpg", "/static/assets/img/property-types/garage.png"],
     /*
    ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.860374, 2.222242, "/index-detail", "assets/img/properties/property-05.jpg", "assets/img/property-types/condominium.png"],
    ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.845917, 2.265673, "/index-detail", "assets/img/properties/property-06.jpg", "assets/img/property-types/cottage.png"],
    ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.843092, 2.306013, "/index-detail", "assets/img/properties/property-07.jpg", "assets/img/property-types/warehouse.png"],
    ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.887697, 2.332277, "/index-detail", "assets/img/properties/property-08.jpg", "assets/img/property-types/apartment.png"],
    ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.871441, 2.347555, "/index-detail", "assets/img/properties/property-07.jpg", "assets/img/property-types/empty.png"],

    ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.832438, 2.369270, "/index-detail", "assets/img/properties/property-09.jpg", "assets/img/property-types/apartment.png"],
    ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.803954, 2.275200, "/index-detail", "assets/img/properties/property-10.jpg", "assets/img/property-types/apartment.png"],
    ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.879183, 2.252133, "/index-detail", "assets/img/properties/property-11.jpg", "assets/img/property-types/construction-site.png"],

     ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.845092, 2.187996, "/index-detail", "assets/img/properties/property-06.jpg", "assets/img/property-types/cottage.png"],
     ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.909218, 2.179756, "/index-detail", "assets/img/properties/property-07.jpg", "assets/img/property-types/single-family.png"],

     ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.910120, 2.352104, "/index-detail", "assets/img/properties/property-01.jpg", "assets/img/property-types/warehouse.png"],
     ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.867681, 2.396736, "/index-detail", "assets/img/properties/property-05.jpg", "assets/img/property-types/empty.png"],
     ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.826109, 2.350731, "/index-detail", "assets/img/properties/property-06.jpg", "assets/img/property-types/industrial-site.png"],
     ['3398 Lodgeville Road', "Golden Valley, MN 55427", "November 16. 2016", 48.794908, 2.353477, "/index-detail", "assets/img/properties/property-03.jpg", "assets/img/property-types/warehouse.png"],
     ['2479 Murphy Court', "Minneapolis, MN 55402", "December 16. 2019", 48.859098, 2.423515, "/index-detail", "assets/img/properties/property-04.jpg", "assets/img/property-types/empty.png"]

     */
];
