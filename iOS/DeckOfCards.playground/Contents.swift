import UIKit

struct Card {
    var value: String
    var Suit: String
    var numerical_value: Int
    
    init(value: String, Suit: String, numerical_value: Int){
        self.value = value
        self.Suit = Suit
        self.numerical_value = numerical_value
    }
    
    func show(){
        print("\(self.value) of \(self.Suit)")
    }
}

class Deck {
    var cards: [Card] = [Card]()
    
    var values: [String] = ["A","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    var suits: [String] = ["Spades", "Diamonds", "Clubs", "Hearts"]
    var num_values: [Int] = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    
    init() {
        self.build()
    }
    
    func build(){
        for suit in suits{
            for i in 0..<num_values.count{
                let card: Card = Card(value: values[i], Suit: suit,numerical_value: num_values[i])
                self.cards.append(card)
            }
        }
    }
    
    func printCards(){
        for card in cards{
            card.show()
        }
        print()
    }
    
    func deal() -> Card{
        return self.cards.removeLast()
        
    }
    
    func reset(){
        self.build()
    }
    
    func shuffle(){
        for i in stride(from: cards.count - 1, through: 0, by: -1){
            let rand: Int = Int(arc4random_uniform(UInt32(i+1)))
            let temp = cards[i]
            cards[i] = cards[rand]
            cards[rand] = temp
        }
        
    }

}

class Player {
    var name:String
    var hand:[Card] = [Card]()
    
    init(name: String){
        self.name = name
    }
    
    func draw(deck: Deck) -> Card {
        let card:Card = deck.deal()
        self.hand.append(card)
        return card
    }
    
    func discard(card: Card) -> Bool{
        var existed: Bool = false
        for i in 0..<hand.count{
            if (hand[i].value == card.value && hand[i].Suit == card.Suit){
                hand.remove(at: i)
                existed = true
            }
        }
        return existed
    }
    
    func printHand(){
        print("Player \(self.name)'s hand:")
        for card in hand{
            card.show()
        }
        print()
    }
}

var deck:Deck = Deck()
deck.printCards()
print()
deck.shuffle()
deck.printCards()
var player: Player = Player(name: "MJ")
player.draw(deck: deck)
player.printHand()
deck.printCards()
