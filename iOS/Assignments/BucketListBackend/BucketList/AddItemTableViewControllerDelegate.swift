//
//  AddItemTableViewControllerDelegate.swift
//  BucketList
//
//  Created by MJ Norona on 7/10/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import Foundation

protocol AddItemTableViewControllerDelegate: class {
    func itemSaved(by controller: AddItemTableViewController, with text: String, index: Int?, at indexPath: NSIndexPath?)
    func cancelButtonPressed(by controller: AddItemTableViewController)
}
