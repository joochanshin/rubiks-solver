import peasy.*;

PeasyCam cam;

int dim = 3;
Box[][][] cube = new Box[dim][dim][dim];
void settings(){
  size(600, 600, P3D);
}
void setup(){

	cam = new PeasyCam(this, 400);
	for (int i = 0; i < dim; i++){
		for (int j = 0; j < dim; j++){
			for (int k = 0; k < dim; k++){
				float len = 50;
				float x = len * i;
				float y = len * j;
				float z = len * k;
				cube[i][j][k] = new Box(x, y, z, len);
			}
		}
	}
}

void draw(){
	background(51);
	for (int i = 0; i < dim; i++){
		for (int j = 0; j < dim; j++){
			for (int k = 0; k < dim; k++){
				cube[i][j][k].show();
			}
		}
	}
	
}

class Box{
	PVector pos;
	float len;

	Box(float x, float y, float z, float len_) {
		pos = new PVector(x,y,z);
		len = len_;
	}
	void show() {
		fill(255);
		stroke(0);
		strokeWeight(8);
		pushMatrix();
		translate(pos.x, pos.y, pos.z);
		box(len);

		popMatrix();
	}
}
