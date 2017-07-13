//
//  ViewController.swift
//  BinaryCounter
//
//  Created by MJ Norona on 7/12/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var tableView: UITableView!

    var numbers: [Int] = []
    
    @IBOutlet weak var sumLabel: UILabel!
    
    var sum: Int = 0;
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        for i in 0..<16 {
            var num = pow(10, i)
            let result = NSDecimalNumber(decimal: num)
            numbers.append(Int(result))
        }
        
        sumLabel.text = "Total: 0"
        

        tableView.dataSource = self
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}

extension ViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return numbers.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "CustomCell") as! CustomCell
        cell.numberLabel.text = String(numbers[indexPath.row])
        cell.tag = indexPath.row
        cell.delegate = self
        return cell
    }
    
    func resetSumLabel() {
        sumLabel.text = "Total \(String(sum))"
    }
    
}

