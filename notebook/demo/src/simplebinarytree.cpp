
/*
g++ -o simplebinarytree simplebinarytree.cpp
./simplebinarytree
*/
#include <iostream>

using namespace std;

template <typename T>
class Node
{
public:
    T data;
    Node *left;
    Node *right;

    Node()
    {
    }

    Node(Node *ileft, Node *iright, const T d)
    {
        data = d;
        if (ileft != NULL)
        {
            Node *left = new Node();
        }
        left = ileft;
        if (iright != NULL)
            Node *right = new Node();
        right = iright;
    }
    
    ~Node()
    {
        if (left != NULL)
            delete left;
        if (right != NULL)
            delete right;
    }

    void getTree_inorder()
    {
        if (left != NULL)
            left->getTree_inorder();
        cout << data << " ";
        if (right != NULL)
            right->getTree_inorder();
    }

    void print_tree()
    {
        cout << "In-order{"
             << " ";
        getTree_inorder();
        cout << "}" << endl;
    }

    void getTree_preorder()
    {
        cout << data << " ";
        if (left != NULL)
            left->getTree_preorder();
        if (right != NULL)
            right->getTree_preorder();
    }

    void print_tree_preorder()
    {
        cout << "pre-order{"
             << " ";
        getTree_preorder();
        cout << "}" << endl;
    }

    void getTree_postorder()
    {
        if (left != NULL)
            left->getTree_postorder();
        if (right != NULL)
            right->getTree_postorder();
        cout << data << " ";
    }

    void print_tree_postorder()
    {
        cout << "post-order{"
             << " ";
        getTree_postorder();
        cout << "}" << endl;
    }
};

int main()
{
    Node<char> *g = new Node<char>(NULL, NULL, 'G');
    Node<char> *e = new Node<char>(NULL, NULL, 'E');
    Node<char> *a = new Node<char>(NULL, NULL, 'A');
    Node<char> *c = new Node<char>(NULL, NULL, 'C');
    Node<char> *b = new Node<char>(a, c, 'B');
    Node<char> *f = new Node<char>(e, g, 'F');
    Node<char> *root = new Node<char>(b, f, 'D');
    root->print_tree();
    root->print_tree_preorder();
    root->print_tree_postorder();
    delete g;
    delete e;
    delete a;
    delete c;
    delete b;
    delete f;
    delete root;
    return 0;
}
