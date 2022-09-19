ArrayList<Platform> p;
boolean iscolliding = false;
PVector pos;
PVector vel;
float moving;
float walk = 5;

void setup() {
  p = new ArrayList<Platform>();
  float y = height/2;
  float ory = y;
  for(int i = 0; i < width/50; i++) {
    p.add(new Platform(i*50, y));
    y += random(-100, 100);
  }
  pos = new PVector(20, ory);
  vel = new PVector();
}
void settings() {
  size(800, 600);
}
void draw() {
  background(000);
  iscolliding = false;
  for(Platform i: p) {
    i.show();
    if(i.collide(pos)) {
      iscolliding = true;
      pos.y = i.pos.y;
    }
  }
  if(pos.y > height) {
    setup();
  }
  if(pos.x > width) {
    setup();
  }
  fill(#00F5FF);
  stroke(0);
  ellipse(pos.x, pos.y-8, 16, 16);
  if(!iscolliding) {
    vel.y += 0.2;
  }
  pos.add(vel);
  pos.x += moving;
  vel.mult(0.9);
  //println(vel.y);
}
void keyPressed() {
  if(key == 'a') {
    moving = -walk;
  }
  if(key == 'd') {
    moving = walk;
  }
  if(key == ' ') {
    if(!iscolliding) {
      vel.y -= 10;
      
    }
  }
}
void keyReleased() {
  if(key == 'a') {
    moving = 0;
  }
  if(key == 'd') {
    moving = 0;
  }
}
