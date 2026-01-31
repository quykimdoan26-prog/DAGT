#include <stdio.h>
void swap(int *x,int *y){
	int temp=*x;
	*x=*y;
	*y=temp;
}
void vundong (int a[],int n, int goc){
	int max=goc;
	int trai=2*goc+1;
	int phai=2*goc+2;
	if (trai<n && a[trai]>a[max]) max=trai;
	if (phai<n && a[phai]>a[max]) max=phai;
	if (max!=goc){
		swap(&a[goc],&a[max]);
		vundong(a,n,max);
	}
}

void sapxep(int a[],int n){
	for (int i=n/2-1; i>=0;i--){
		vundong(a,n,i);
	}
	for (int i=n-1;i>=0;i--){
		swap(&a[0],&a[i]);
		vundong (a,i,0);
	}}
int timkiemnhiphan(int a[],int n,int gtct){
		int trai=0;
		int phai=n-1;
		
		while (trai<=phai){
            int giua=(trai+phai)/2;
		if (a[giua]==gtct) return giua;
		else{
			if (giua>gtct) phai=giua-1;
			else trai=giua+1;
		}
			}
		return -1;
	}
int cnt[1000];
int main (){
	int a[100],n;
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",&a[i]);
}
     sapxep(a,n);
     for (int i=0;i<n;i++) printf ("%d ",a[i]);
     printf("\n");
	int gtct;
	printf ("nhap gia tri can tim:");
	scanf("%d",&gtct);
	int vitri=timkiemnhiphan(a,n,gtct);
   if( vitri>=0&&vitri<=n) printf("gia tri %d o dia chi a[%d]",gtct,vitri);
	
	return 0;
}

struct Node{
	int data;
	Node*trai;
	Node*phai;
};

Node*deleteBST(Node*root,int x){
	if(root=nullptr) return nullptr;
	if(x>root->data) root->phai=deleteBST(root->phai,x);
	else if(x<root->data) root->trai=deleteBST(root->trai,x);
	if(x==root->data){
		if(root->trai==nullptr){
			Node *temp=root->phai;
			delete root;
			return temp;
		}
		else if(root->phai==nullptr){
			Node *temp=root->trai;
			delete root;
			return temp;
		}
		Node *temp=fidmin(root->phai);
		root->data=temp->data;
		root->phai=deleteBST(root->phai,x)

}
  }