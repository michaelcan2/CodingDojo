﻿// <auto-generated />
using BankAccount.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage;
using Microsoft.EntityFrameworkCore.Storage.Internal;
using System;

namespace BankAccount.Migrations
{
    [DbContext(typeof(BankAccountContext))]
    [Migration("20180516004947_first")]
    partial class first
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn)
                .HasAnnotation("ProductVersion", "2.0.2-rtm-10011");

            modelBuilder.Entity("BankAccount.Models.Transaction", b =>
                {
                    b.Property<int>("id")
                        .ValueGeneratedOnAdd();

                    b.Property<double>("amount");

                    b.Property<int>("userid");

                    b.HasKey("id");

                    b.HasIndex("userid");

                    b.ToTable("Transactions");
                });

            modelBuilder.Entity("BankAccount.Models.User", b =>
                {
                    b.Property<int>("id")
                        .ValueGeneratedOnAdd();

                    b.Property<double?>("balance");

                    b.Property<string>("email");

                    b.Property<string>("first_name");

                    b.Property<string>("last_name");

                    b.Property<string>("password");

                    b.HasKey("id");

                    b.ToTable("Users");
                });

            modelBuilder.Entity("BankAccount.Models.Transaction", b =>
                {
                    b.HasOne("BankAccount.Models.User", "user")
                        .WithMany("transactions")
                        .HasForeignKey("userid")
                        .OnDelete(DeleteBehavior.Cascade);
                });
#pragma warning restore 612, 618
        }
    }
}
