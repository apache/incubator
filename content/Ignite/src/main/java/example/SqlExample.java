/*
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
*/
package example;

import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.StringJoiner;
import javax.cache.Cache;
import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.QueryEntity;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.cache.query.SqlQuery;
import org.apache.ignite.cache.query.annotations.QuerySqlField;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.lang.IgniteBiPredicate;

public class SqlExample {

    public static class Customer {
        private long id = -1;

        @QuerySqlField
        private String name;

        // tag::field[]
        @QuerySqlField
        private String email;

        @QuerySqlField(index = true)
        private String phoneNumber;
        // end::field[]

        public Customer(int id, String name, String email, String phoneNumber) {
            this.id = id;
            this.name = name;
            this.email = email;
            this.phoneNumber = phoneNumber;
        }

        @Override public String toString() {
            return new StringJoiner(", ", Customer.class.getSimpleName() + "[", "]")
                .add("id=" + id)
                .add("name='" + name + "'")
                .add("email='" + email + "'")
                .add("phoneNumber='" + phoneNumber + "'")
                .toString();
        }
    }

    public static void main(String[] args) {
        IgniteConfiguration cfg = new IgniteConfiguration();
        try (Ignite ignite = Ignition.start(cfg)) {

            // tag::entity[]
            CacheConfiguration<Long, Customer> ccfg = new CacheConfiguration<>("customer");
            ccfg.setQueryEntities(Collections.singletonList(new QueryEntity(Long.class, Customer.class)));
            // end::entity[]
            IgniteCache<Long, Customer> cache = ignite.getOrCreateCache(ccfg);
            Customer client = new Customer(777200, "Jennifer Stain", "jenny@test.com", "+1-541-754-3010");
            System.out.println("Saving client " + client);
            cache.put(client.id, client);

            // tag::scan[]
            IgniteBiPredicate<Long, Customer> filter
                = (Long k, Customer v) -> v.email != null && v.email.contains("@test.com");

            try (QueryCursor<Cache.Entry<Long, Customer>> cursor
                     = cache.query(new ScanQuery<Long, Customer>().setFilter(filter))) {
                for (Cache.Entry<Long, Customer> entry : cursor.getAll())
                    System.out.println(entry.getValue().name + " " + entry.getValue().phoneNumber);
            }
            // end::scan[]

            // tag::query[]
            String phoneNum = "+1-541-754-3010";
            try (QueryCursor<Cache.Entry<Long, Customer>> qry
                     = cache.query(new SqlQuery<Long, Customer>(Customer.class, "where phoneNumber = ?")
                .setArgs(phoneNum))) {

                for (Cache.Entry<Long, Customer> entry : qry) {
                    Customer val = entry.getValue();
                    System.out.println("Customer found " + val);
                }
            }
            // end::query[]

            // tag::fields[]
            SqlFieldsQuery qry = new SqlFieldsQuery("select concat(name, ' <', email, '>') from Customer");

            // Execute query to get collection of rows. In this particular
            // case each row will have one element with full name formatted in Git-style
            Collection<List<?>> res = cache.query(qry).getAll();

            // Print names.
            System.out.println("Names of all customers:" + res);
            // end::fields[]
        }
    }
}
