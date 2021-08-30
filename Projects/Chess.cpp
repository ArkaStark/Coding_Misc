#include<bits/stdc++.h>
#include<cmath>
#include<iostream>
using namespace std;

// To represent a general piece and functionalities common to all pieces

class Piece{
    private:
        bool killed = false;
        bool white = false;
    
    public:
        Piece(bool white=true){
            this->setWhite(white);
        }

        bool isWhite(){
            return this->white;
        }

        void setWhite(bool white){
            this->white = white;
        }

        bool isKilled(){
            return this->killed;
        }

        void setKilled(bool killed){
            this->killed = killed;
        }

        virtual bool canMove(Board board, Spot from, Spot to);
};

// To represent a cell on the chessboard.

class Spot{
    private:
        Piece piece;
        int x;
        int y;

    public:
        Spot(int x, int y, Piece piece){
            this->setPiece(piece);
            this->setX(x);
            this->setY(y);
        } 

        Piece getPiece(){
            return this->piece;
        }

        void setPiece(Piece p){
            this->piece = p;
        }

        int getX(){
            return this->x;
        }

        void setX(int x){
            this->x = x;
        }

        int getY(){
            return this->y;
        }

        void setY(int y){
            this->y = y;
        }
};


class King : public Piece{
    private:
        bool castled = false;

    public:
        King(bool white): Piece(white){}

        bool isCastled(bool castled){
            return this->castled;
        }

        void castle(bool castled){
            if(!castled)
                this->castled = true;
        }

        bool canMove(Board board, Spot from, Spot to) override{
            if(to.getPiece().isWhite() == this->isWhite()){
                return false;
            }

            int x = abs(from.getX() - to.getX());
            int y = abs(from.getY() - to.getY());
            if(x+y == 1)
                return true;
        }

};


class Knight : public Piece {
    public:
    Knight(bool white) : Piece(white){}

  
    bool canMove(Board board, Spot start, Spot end)
    {
        // we can't move the piece to a spot that has
        // a piece of the same colour
        if (end.getPiece().isWhite() == this->isWhite()) {
            return false;
        }
  
        int x = abs(start.getX() - end.getX());
        int y = abs(start.getY() - end.getY());
        return x * y == 2;
    }
};

class Board {
    Spot* boxes[8][8];
  
    public:
    Board()
    {
        this->resetBoard();
    }

    Spot getBox(int x, int y)
    {
        return *boxes[x][y];
    }
  
    void resetBoard()
    {
        // initialize white pieces
        boxes[0][1] = new Spot(0, 1, new Knight(true));

  
        // initialize black pieces
        boxes[7][1] = new Spot(7, 1, new Knight(false));
  
        // initialize remaining boxes without any piece
        for (int i = 2; i < 6; i++) {
            for (int j = 0; j < 8; j++) {
                boxes[i][j] = new Spot(i, j, NULL);
            }
        }
    }
};

class Player {
    public:
    bool whiteSide;
    bool humanPlayer;
    bool isWhiteSide()
    {
        return this->whiteSide;
    }
    public:
    bool isHumanPlayer()
    {
        return this->humanPlayer;
    }
};
  
class HumanPlayer : public Player {
  
    public:
    HumanPlayer(bool whiteSide)
    {
        this->whiteSide = whiteSide;
        this->humanPlayer = true;
    }
};
  
class ComputerPlayer : public Player {
  
    public:
    ComputerPlayer(bool whiteSide)
    {
        this->whiteSide = whiteSide;
        this->humanPlayer = false;
    }
};



class Move {
    private:
    Player player;
    Spot start;
    Spot end;
    Piece pieceMoved;
    Piece pieceKilled;
    bool castlingMove = false;
  
    public:
    Move(Player player, Spot start, Spot end)
    {
        this->player = player;
        this->start = start;
        this->end = end;
        this->pieceMoved = start.getPiece();
    }
  
    bool isCastlingMove()
    {
        return this->castlingMove;
    }
  
    void setCastlingMove(bool castlingMove)
    {
        this->castlingMove = castlingMove;
    }
};



enum GameStatus {
    ACTIVE,
    BLACK_WIN,
    WHITE_WIN,
    FORFEIT,
    STALEMATE,
    RESIGNATION
};



class Game {
    private:
    Player players[2];
    Board board;
    Player currentTurn;
    GameStatus status;
    list<Move> movesPlayed;
  
    void initialize(Player p1, Player p2)
    {
        players[0] = p1;
        players[1] = p2;
  
        board.resetBoard();
  
        if (p1.isWhiteSide()) {
            this->currentTurn = p1;
        }
        else {
            this->currentTurn = p2;
        }
  
        movesPlayed.clear();
    }
  
    public:
    bool isEnd()
    {
        return this->getStatus() != ACTIVE;
    }
  
    bool getStatus()
    {
        return this->status;
    }
  
    void setStatus(GameStatus status)
    {
        this->status = status;
    }
  
    bool playerMove(Player player, int startX, int startY, int endX, int endY)
    {
        Spot startBox = board.getBox(startX, startY);
        Spot endBox = board.getBox(startY, endY);
        Move* move = new Move(player, startBox, endBox);
        return this->makeMove(*move, player);
    }
  
    bool makeMove(Move move, Player player)
    {
        Piece sourcePiece = move.getStart().getPiece();
        if (sourcePiece == NULL) {
            return false;
        }
  
        // valid player
        if (player != currentTurn) {
            return false;
        }
  
        if (sourcePiece.isWhite() != player.isWhiteSide()) {
            return false;
        }
  
        // valid move?
        if (!sourcePiece.canMove(board, move.getStart(), move.getEnd())) {
            return false;
        }
  
        // kill?
        Piece destPiece = move.getStart().getPiece();
        if (destPiece != NULL) {
            destPiece.setKilled(true);
            move.setPieceKilled(destPiece);
        }
  
        // castling?
        if (sourcePiece != NULL && sourcePiece instanceof King && sourcePiece.isCastlingMove()) {
            move.setCastlingMove(true);
        }
  
        // store the move
        movesPlayed.add(move);
  
        // move piece from the stat box to end box
        move.getEnd().setPiece(move.getStart().getPiece());
        move.getStart().setPiece(NULL);
  
        if (destPiece != null && destPiece instanceof King) {
            if (player.isWhiteSide()) {
                this->setStatus(WHITE_WIN);
            }
            else {
                this->setStatus(BLACK_WIN);
            }
        }
  
        // set the current turn to the other player
        if (this->currentTurn == players[0]) {
            this->currentTurn = players[1];
        }
        else {
            this->currentTurn = players[0];
        }
  
        return true;
    }
};