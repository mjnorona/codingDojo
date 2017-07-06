import UIKit

class Animal {
    var name: String
    var health: Int
    init(name: String){
        self.name = name
        self.health = 100
    }
    
    func displayHealth(){
        print("Health \(health)")
    }
}

class Cat: Animal {
    
    override init(name: String){
        super.init(name: name)
        self.health = 150
    }
    
    func growl(){
        print("Rawr!")
    }
    
    func run(){
        print("Running")
        self.health -= 10
    }
}

//var cat: Cat = Cat(name: "Billy")
//cat.growl()
//cat.run()
//cat.displayHealth()

class Cheetah: Cat {
    override func run(){
        if (health >= 50){
            print("Running Fast")
            self.health -= 50
        }
        else {
            print("Not enough health")
        }
    }
}

class Lion: Cat{
    
    override init(name: String){
        super.init(name: name)
        self.health = 200
    }
    
    override func growl() {
        print("ROAR!!!! I am the King of the Jungle")
    }
}

var cheetah: Cheetah = Cheetah(name: "Bob")
cheetah.run()
cheetah.run()
cheetah.run()
cheetah.run()
cheetah.displayHealth()

var lion: Lion = Lion(name: "Billy")
lion.run()
lion.run()
lion.run()
lion.displayHealth()
