include <roundedcube.scad>;


module nappi () 
difference(){
  cylinder(d=17,h=4);
  translate([0,0,-1])cylinder(d=13,h=6);
}

module nappis() 
  for (y=[0:16:70])
    for (x=[0:16:50])
      translate([x,y,0])  nappi();

module levy() color("RED") difference() {
  union() {
      cube([80,110,2]);
      translate([15,30,2])nappis();
      translate([39,15,2])nappi();
    }
  translate([15,30,0])
    for (y=[0:16:70])
      for (x=[0:16:50])
	translate([x,y,0]) cylinder(d=2,h=10) ;
  translate([39,15,0])cylinder(d=2,h=10) ;
}

module boxi() {
  difference(){
    roundedcube([90,120,30],radius=5);
    translate([2,2,-4])roundedcube([86,116,30],radius=3);
    translate([42,115,0])  cube([5,10,18]);
    translate([10,10,10])roundedcube([70,100,40],radius=3);
  }
}

module pohja()
translate([2.5,2.5,0])
  difference(){
  roundedcube([85,115,30],radius=3);
  translate([2,2,2])roundedcube([80,110,20],radius=1);
  translate([-1,-1,20])cube([90,120,20]);
} 
module kaikki() {
  boxi();
  translate([5,5,24])levy();
  translate([0,0,-5])  pohja();
}
//kaikki();
pohja();


